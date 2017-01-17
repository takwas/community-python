from ..blueprint import admin
from models import Module, Module_Type
from flask import render_template, redirect, flash, url_for

@admin.route('/modules')
def modules():
    modules = Module.select()
    module_types = Module_Type.select()

    return render_template('modules/index.html', modules=modules, module_types=module_types)


@admin.route('/module/<module_id>')
def module(module_id):
    module = Module.select().where(Module.id == module_id)

    if not module.exists():
        flash('Module bestaat niet.')
        return redirect(url_for('admin.modules'))

    module = module.get()

    return render_template('modules/module.html', module=module)
