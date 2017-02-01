from models import initialize_db, close_db_connection
from .blueprint import auth
from .controllers import RegistrationController, AuthenticationController, LogoutController


@auth.before_request
def before_request():
    initialize_db()


@auth.teardown_request
def teardown_request(exception):
    close_db_connection()
