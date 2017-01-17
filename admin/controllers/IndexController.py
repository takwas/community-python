from ..blueprint import admin
from models import User, Group
from flask import render_template, redirect, url_for


# testing route
@admin.route('/test')
def test():
    group = Group(name='Test', description='test description')
    group.save()
    return redirect(url_for('admin.index'))


@admin.route('/')
def index():
    users_count = User.select().count()
    last_registered_user = User.select().order_by(User.registered_on.desc()).get()

    # TODO: fix if no groups
    group_count = Group.select().count()
    last_created_group = Group.select().order_by(Group.created_on.desc()).get()

    return render_template(
        'home.html',
        users_count=users_count,
        last_registered_user=last_registered_user,
        group_count=group_count,
        last_created_group=last_created_group
    )
