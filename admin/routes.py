from flask import Blueprint, render_template, redirect, url_for, session
from models import initialize_db, close_db_connection, User
import bcrypt
from middleware import LoginMiddleWare

admin = Blueprint(
    'admin', __name__, template_folder='templates',
    static_folder='static')


@admin.before_request
@LoginMiddleWare.login_required
def before_request():
    initialize_db()


@admin.teardown_request
def teardown_request(exception):
    close_db_connection()


@admin.route('/')
def index():
    return render_template('home.html')


@admin.route('/users')
def users():
    users = User.select()
    return render_template('users/users.html', users=users)


@admin.route('/users/new', methods=['POST'])
def new_user():
    hashed = bcrypt.hashpw('test', bcrypt.gensalt())
    user = User(fname='Erik', sname='Hoofd', email='ehoofd@gmail.com',
        password=hashed)
    user.save()
    return redirect(url_for('admin.users'))
