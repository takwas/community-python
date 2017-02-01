from flask import redirect, url_for, session
from models import initialize_db, close_db_connection
from .blueprint import auth
from middleware import AuthMiddleware
from .controllers import RegistrationController, AuthenticationController


@auth.before_request
def before_request():
    initialize_db()


@auth.teardown_request
def teardown_request(exception):
    close_db_connection()


@auth.route('/logout')
@AuthMiddleware.login_required
def logout():
    session.pop('user', None)
    return redirect(url_for('auth.login'))
