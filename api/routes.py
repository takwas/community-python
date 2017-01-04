from flask import Blueprint
from models import initialize_db, close_db_connection

api = Blueprint('api', __name__)


@api.before_request
def before_request():
    initialize_db()


@api.teardown_request
def teardown_request(exception):
    close_db_connection()


@api.route('/')
def index():
    return "api index"
