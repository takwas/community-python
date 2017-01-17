from models import initialize_db, close_db_connection
from .blueprint import register


@register.before_request
def before_request():
    initialize_db()


@register.teardown_request
def teardown_request(exception):
    close_db_connection()

@register.route('/')
def index():
    return 'index register'