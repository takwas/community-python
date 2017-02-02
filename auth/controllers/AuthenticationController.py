from ..blueprint import auth
from models import User, User_Role, Role
from flask import redirect, url_for, request, make_response, jsonify, flash, current_app, session, render_template
from playhouse.shortcuts import model_to_dict
import datetime
import jwt
import bcrypt
from middleware import AuthMiddleware
from helpers import validate
from enums.auth import AuthRoleType
from ..forms.register import SimpleLoginForm


@auth.route('/authenticate-jwt')
@AuthMiddleware.no_login_required
def authenticate():
    email = request.args.get('email')
    password = request.args.get('password')

    # check for required params
    if not email or not password:
        resp = make_response(jsonify({'error': 'Required data not found'}), 400)
        return resp

    # select user
    user = User.select().where(User.email == email).where(User.activated == True)

    # check if user exists
    if not user.exists():
        resp = make_response(jsonify({'error': 'User not found or account not yet activated'}), 404)
        return resp

    user = user.get()

    # check password
    right_password = bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))
    if not right_password:
        resp = make_response(jsonify({'error': 'Email or password combination not falid'}), 400)
        return resp

    # make JWT hash
    # TODO: fix json serialization
    user.registered_on = str(user.registered_on)
    user.uuid = str(user.uuid)

    encoded = jwt.encode({'user': model_to_dict(user), 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24 * 30)}, current_app.secret_key, algorithm='HS256').decode('utf-8')
    response = {'jwt': encoded, 'user': model_to_dict(user)}
    return jsonify(response)


@auth.route('/login', methods=['GET', 'POST'])
@AuthMiddleware.no_login_required
def login():
    form = SimpleLoginForm(request.form)

    # login post method
    if request.method == 'POST' and form.validate():
        email = request.form['email']
        password = request.form['password']

        # check for required values
        if not email or not password:
            flash('Vul alles in')
            return redirect(url_for('auth.login'))

        # get user object
        user = User.select().where(User.email == email).where(User.activated == True)

        # check if account exists
        if not user.exists():
            flash('Geen gebruiker gevonden met dit email of het account is not niet geactiveerd')
            return redirect(url_for('auth.login'))

        user = user.get()

        # check password
        right_password = bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))
        if not right_password:
            flash('Foutive inloggegevens')
            return redirect(url_for('auth.login'))

        # check us user has admin role
        assigned_roles = user.assigned_roles
        if len(assigned_roles) > 0:
            access = True
        else:
            access = False

        # check admin role
        if access is False:
            flash('U kunt niet inloggen')
            return redirect(url_for('auth.login'))

        # add user to session
        session['user'] = model_to_dict(user)  # convert to dict

        # to role switching page
        return redirect(url_for('auth.switch_role'))

    # login page
    else:
        return render_template('pages/login.html', form=form)


@auth.route('/switch-role', methods=['GET', 'POST'])
@AuthMiddleware.login_required
def switch_role():
    """
    Switch role view and logic
    Switch role based on assigned roles and add to session
    """
    u = User.from_object(session['user'])
    roles = u.assigned_roles

    if request.method == 'POST':
        role_value = request.form['role']
        if not role_value:
            flash('Kiez een rol')
            return redirect(url_for('auth.switch_role'))

        role = Role.select().where(Role.id == role_value)
        if not role.exists():
            flash('Rol bestaat niet')
            return redirect(url_for('auth.switch_role'))

        role = role.get()

        # check if user has selected role
        for r in roles:
            if role == r.role:
                session['active_role'] = model_to_dict(role)
                # ADMIN
                if role.role == AuthRoleType.ADMIN.value:
                    return redirect(url_for('admin.index'))
                # CLIENT
                elif role.role == AuthRoleType.CLIENT.value:
                    return redirect('/client/')
                else:
                    return redirect('/')

        flash('U heeft de gekozen rol niet')
        return redirect(url_for('auth.switch_role'))

    return render_template('pages/switch_role.html', roles=roles)


@auth.route('/activate/<user_uuid>/<activation_key>')
@AuthMiddleware.no_login_required
def activate(user_uuid, activation_key):
    # check for valid uuid
    if not validate.uuid_validation(user_uuid):
        flash('Ongeldige gegevens')
        return redirect(url_for('auth.login'))

    user = User.select().where(User.uuid == user_uuid).where(User.activation_key == activation_key)

    if not user.exists():
        flash('Foutive activatie gegevens')
        return redirect(url_for('auth.login'))

    user = user.get()

    # if account is alreadt activated
    if user.activated is True:
        flash('Account is al geactiveerd')
        return redirect(url_for('auth.login'))

    user.activated = True
    user.save()

    role, created = Role.get_or_create(role='client')

    new_role = User_Role.create(user=user, role=role)

    flash('Account geactiveerd')
    return redirect(url_for('auth.login'))
