from ..blueprint import admin
from models import User
from flask import render_template


@admin.route('/users')
def users():
    all_users = User.select()
    return render_template('users/users.html', users=all_users)