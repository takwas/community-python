from ..blueprint import admin
from models import Module, Module_Type, Module_Location, Location
from flask import render_template, redirect, flash, url_for, request
from datetime import datetime

@admin.route('/modules')
def modules():
    modules = Module.select().order_by(Module.build_on.desc())
    module_types = Module_Type.select()

    return render_template('modules/index.html', modules=modules, module_types=module_types)


@admin.route('/modules/module/<module_id>')
def module(module_id):
    module = Module.select().where(Module.id == module_id)

    if not module.exists():
        flash('Module bestaat niet.')
        return redirect(url_for('admin.modules'))

    module = module.get()

    module_locatons = Module_Location.select().where(Module_Location.module == module).order_by(Module_Location.start_date.desc()).limit(5)

    locations = Location.select().where(Location.unavailable_from > datetime.now().date())

    return render_template('modules/module.html', module=module, locations=module_locatons, available_locations=locations, datetime=datetime)


@admin.route('/modules/module/<module_id>/new_location', methods=['POST'])
def new_module_location(module_id):
    _location = request.form['location']
    _placed_on = request.form['placed_on']
    _placed_til = None if not request.form['placed_til'] else request.form['placed_til']

    #
    # check if module exists
    #
    module = Module.select().where(Module.id == module_id)

    if not module.exists():
        flash('Module bestaat niet.')
        return redirect(url_for('admin.modules'))

    module = module.get()

    #
    # check if data is valid
    #
    if not _location or not _placed_on or not _placed_til:
        flash('Verplichte velden niet ingevuld.')
        return redirect(url_for('admin.module', module_id=module.id))

    if _placed_on > _placed_til:
        flash('Module kan niet eerder weggehaald worden dan geplaatst.')
        return redirect(url_for('admin.module', module_id=module.id))

    #
    # check if location exists
    #
    location = Location.select().where(Location.id == _location)

    if not location.exists():
        flash('Locatie bestaat niet.')
        return redirect(url_for('admin.module', module_id=module.id))

    location = location.get()

    #
    # check if location is still available
    #
    if datetime.strptime(_placed_on, '%Y-%m-%d').date() > location.unavailable_from or datetime.strptime(_placed_til, '%Y-%m-%d').date() > location.unavailable_from:
        flash('Locatie niet meer beschikbaar dan.')
        return redirect(url_for('admin.module', module_id=module.id))

    #
    # check if module is still placed
    #
    q = Module_Location.select().where(Module_Location.module == module).where((Module_Location.start_date.between(_placed_on, _placed_til)) | (Module_Location.end_date.between(_placed_on, _placed_til)))

    if q.exists():
        flash('Module dan nog geplaatst.')
        return redirect(url_for('admin.module', module_id=module.id))

    #
    # add new module location
    #
    Module_Location.create(module=module, location=location, start_date=_placed_on, end_date=_placed_til)

    return redirect(url_for('admin.module', module_id=module.id))


@admin.route('/module/new', methods=['POST'])
def new_module():
    type = Module_Type.select().where(Module_Type.id == request.form['module_type'])

    if not type.exists():
        flash('Module type bestaat niet.')
        return redirect(url_for('admin.modules'))

    module = Module(type=type)
    module.save()
    return redirect(url_for('admin.modules'))