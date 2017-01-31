from ..blueprint import admin
from models import User, Group, Module
from flask import render_template, redirect, url_for
import uuid


# testing route
@admin.route('/test')
def test():
    print(uuid.getnode())
    print(uuid.uuid1())
    print(uuid.uuid4())
    return redirect(url_for('admin.index'))


@admin.route('/')
def index():
    users_count = User.select().count()
    last_registered_user = User.select().order_by(User.registered_on.desc()).get()
    modules = Module.select()

    last_created_group = Group.select().order_by(Group.created_on.desc())

    if last_created_group.exists():
        last_created_group = last_created_group.get()

    group_count = Group.select().count()

    return render_template(
        'home.html',
        users_count=users_count,
        last_registered_user=last_registered_user,
        group_count=group_count,
        last_created_group=last_created_group,
        modules=modules
    )
