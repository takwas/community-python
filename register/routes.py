from models import initialize_db, close_db_connection
from .blueprint import register
from middleware import AuthMiddleware

from .controllers import RegistrationController


@register.before_request
@AuthMiddleware.no_login_required
def before_request():
    initialize_db()


@register.teardown_request
def teardown_request(exception):
    close_db_connection()
