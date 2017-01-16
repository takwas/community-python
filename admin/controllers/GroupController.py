from ..blueprint import admin
from models import Group
from flask import render_template


@admin.route('/groups')
def groups():
    all_groups = Group.select()
    return render_template('groups/groups.html', groups=all_groups)