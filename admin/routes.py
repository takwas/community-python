from flask import Blueprint, render_template, redirect, url_for
from models import initialize_db, close_db_connection, User, Group
import bcrypt
from middleware import login_required

admin = Blueprint(
    'admin', __name__,
    template_folder='templates',
    static_folder='static'
)


@admin.before_request
@login_required
def before_request():
    initialize_db()


@admin.teardown_request
def teardown_request(exception):
    close_db_connection()


@admin.route('/')
def index():
    users_count = User.select().count()
    last_registered_user = User.select().order_by(User.registered_on.desc()).get()

    group_count = Group.select().count()
    last_created_group = Group.select().order_by(Group.created_on.desc()).get()

    return render_template(
        'home.html',
        users_count=users_count,
        last_registered_user=last_registered_user,
        group_count=group_count,
        last_created_group=last_created_group
    )


@admin.route('/users')
def users():
    users = User.select()
    return render_template('users/users.html', users=users)


@admin.route('/users/new', methods=['POST'])
def new_user():
    hashed = bcrypt.hashpw('test', bcrypt.gensalt())
    user = User(fname='Erik', sname='Hoofd', email='ehoofd@gmail.com', password=hashed)
    user.save()
    return redirect(url_for('admin.users'))


@admin.route('/groups')
def groups():
    groups = Group.select()
    return render_template('groups/groups.html', groups=groups)
