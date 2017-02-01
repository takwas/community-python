from ..blueprint import auth
from models import User
from flask import redirect, url_for, request, make_response, jsonify, flash, current_app, session, render_template
from playhouse.shortcuts import model_to_dict
import datetime
import jwt
import bcrypt
from middleware import AuthMiddleware
from helpers.validate import uuid_validation


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
    user.registered_on = str(user.registered_on)
    encoded = jwt.encode({'user': model_to_dict(user), 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24 * 30)}, current_app.secret_key, algorithm='HS256')
    response = {'jwt': encoded, 'user': model_to_dict(user)}
    return jsonify(response)


@auth.route('/login', methods=['GET', 'POST'])
@AuthMiddleware.no_login_required
def login():
    # login post method
    if request.method == 'POST':
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

        # check us user has admin role
        access = False
        for assigned_role in user.assigned_roles:
            if assigned_role.role.role == 'admin':
                access = True

        # check admin role
        if access is False:
            flash('U bent geen admin')
            return redirect(url_for('auth.login'))

        # check password
        right_password = bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))
        if not right_password:
            flash('Foutive inloggegevens')
            return redirect(url_for('auth.login'))

        # add user to session
        session['user'] = model_to_dict(user)  # convert to dict
        session['user_language'] = request.headers.get('Accept-Language')
        flash('succesvol ingelogd')
        return redirect(url_for('admin.index'))

    # login page
    else:
        return render_template('login.html')


@auth.route('/activate/<user_uuid>/<activation_key>')
@AuthMiddleware.no_login_required
def activate(user_uuid, activation_key):
    # check for valid uuid
    if not uuid_validation(user_uuid):
        flash('Ongeldige gegevens')
        return redirect(url_for('auth.login'))

    user = User.select().where(User.uuid == user_uuid).where(User.activation_key == activation_key)

    if not user.exists():
        flash('Foutive activatie gegevens')
        return redirect(url_for('auth.login'))

    user = user.get()

    if user.activated is True:
        flash('Account is al geactiveerd')
        return redirect(url_for('auth.login'))

    user.activated = True
    user.save()

    flash('Account geactiveerd')
    return redirect(url_for('auth.login'))
