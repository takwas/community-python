from ..blueprint import admin
from models import User
from flask import render_template


@admin.route('/users')
def users():
    users = User.select()
    return render_template('users/users.html', users=users)
