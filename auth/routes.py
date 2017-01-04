from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from models import initialize_db, close_db_connection, User
from playhouse.shortcuts import model_to_dict
import bcrypt

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

    #login page
    else:
        return render_template('login.html')


@auth.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('auth.login'))
