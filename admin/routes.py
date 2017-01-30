from models import initialize_db, close_db_connection
from middleware import login_required
from .blueprint import admin
from .controllers import IndexController, UserController, GroupController, ContractController, ModuleController, LocationController, ApiController


@admin.before_request
@login_required
def before_request():
    initialize_db()


@admin.teardown_request
def teardown_request(exception):
    close_db_connection()
