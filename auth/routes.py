from flask import Blueprint, render_template, redirect, url_for, request, flash, session, jsonify, make_response, current_app
from playhouse.shortcuts import model_to_dict
from models import initialize_db, close_db_connection, User
import bcrypt
import jwt

auth = Blueprint('auth', __name__, template_folder='templates')


@auth.before_request
def before_request():
    initialize_db()


@auth.teardown_request
def teardown_request(exception):
    close_db_connection()


@auth.route('/register')
def register():
    hashed = bcrypt.hashpw('test', bcrypt.gensalt())
    user = User(
        fname='Theo',
        sname='Bouwman',
        email='theobouwman98@gmail.com',
        password=hashed
    )
    user.save()
    return redirect(url_for('auth.login'))


@auth.route('/authenticate-jwt')
def authenticate():
    email = request.args.get('email')
    password = request.args.get('password')

    # check for required params
    if not email or not password:
        resp = make_response(jsonify({'error': 'Required data not found'}), 400)
        return resp

    # select user
    user = User.select().where(User.email == email)

    # check if user exists
    if not user.exists():
        resp = make_response(jsonify({'error': 'User not found'}), 404)
        return resp

    user = user.get()

    # check password
    right_password = bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))
    if not right_password:
        resp = make_response(jsonify({'error': 'Email or password combination not falid'}), 400)
        return resp

    # make JWT hash
    encoded = jwt.encode({'user': user.email}, current_app.secret_key, algorithm='HS256')
    response = {'jwt': encoded, 'user': model_to_dict(user)}
    return jsonify(response)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    # login post method
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if not email or not password:
            return redirect(url_for('auth.login'))

        user = User.select().where(User.email == email)
        # check if account exists
        if not user.exists():
            flash('Geen gebruiker gevonden met dit email')
            return redirect(url_for('auth.login'))

        # check password
        right_password = bcrypt.checkpw(password.encode('utf-8'), user.get().password.encode('utf-8'))
        if not right_password:
            flash('Foutive inloggegevens')
            return redirect(url_for('auth.login'))

        print model_to_dict(user.get())
        session['user'] = model_to_dict(user.get())  # convert to dict
        flash('succesvol ingelogd')
        return redirect(url_for('admin.index'))

    # login page
    else:
        return render_template('login.html')


@auth.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('auth.login'))
