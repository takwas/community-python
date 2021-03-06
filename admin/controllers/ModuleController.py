from helpers.enums import AlertType
from middleware import ValidationMiddleware
from ..blueprint import admin
from models import Module, Module_Type, Module_Location, Location
from flask import render_template, redirect, flash, url_for, request
from datetime import datetime


@admin.route('/modules')
def modules():
    modules = Module.select().order_by(Module.build_on.desc())
    module_types = Module_Type.select()

    return render_template('modules/index.html', modules=modules, module_types=module_types)


@admin.route('/modules/module/<module_uuid>')
@ValidationMiddleware.uuid_validation(redirect_url='admin.modules')
def module(module_uuid):
    module = Module.select().where(Module.uuid == module_uuid)

    if not module.exists():
        flash('Module bestaat niet.', AlertType.WARNING.value)
        return redirect(url_for('admin.modules'))

    module = module.get()

    module_locatons = Module_Location.select().where(Module_Location.module == module).order_by(Module_Location.start_date.desc()).limit(5)

    locations = Location.select().where(Location.unavailable_from > datetime.now().date())

    return render_template('modules/module.html', module=module, locations=module_locatons, available_locations=locations, datetime=datetime)


@admin.route('/modules/module/<module_uuid>/new_location', methods=['POST'])
@ValidationMiddleware.uuid_validation('admin.modules')
def new_module_location(module_uuid):
    _location = request.form['location']
    _placed_on = request.form['placed_on']
    _placed_til = None if not request.form['placed_til'] else request.form['placed_til']

    #
    # check if module exists
    #
    module = Module.select().where(Module.uuid == module_uuid)

    if not module.exists():
        flash('Module bestaat niet.', AlertType.WARNING.value)
        return redirect(url_for('admin.modules'))

    module = module.get()

    #
    # check if data is valid
    #
    if not _location or not _placed_on or not _placed_til:
        flash('Verplichte velden niet ingevuld.', AlertType.WARNING.value)
        return redirect(url_for('admin.module', module_uuid=module.uuid))

    if _placed_on > _placed_til:
        flash('Module kan niet eerder weggehaald worden dan geplaatst.', AlertType.WARNING.value)
        return redirect(url_for('admin.module', module_uuid=module.uuid))

    #
    # check if location exists
    #
    location = Location.select().where(Location.id == _location)

    if not location.exists():
        flash('Locatie bestaat niet.', AlertType.WARNING.value)
        return redirect(url_for('admin.module', module_uuid=module.uuid))

    location = location.get()

    #
    # check if location is still available
    #
    if datetime.strptime(_placed_on, '%Y-%m-%d').date() > location.unavailable_from or datetime.strptime(_placed_til, '%Y-%m-%d').date() > location.unavailable_from:
        flash('Locatie niet meer beschikbaar dan.', AlertType.WARNING.value)
        return redirect(url_for('admin.module', module_uuid=module.uuid))

    #
    # check if module is still placed
    #
    q = Module_Location.select().where(Module_Location.module == module).where((Module_Location.start_date.between(_placed_on, _placed_til)) | (Module_Location.end_date.between(_placed_on, _placed_til)))

    if q.exists():
        flash('Module dan nog geplaatst.', AlertType.WARNING.value)
        return redirect(url_for('admin.module', module_uuid=module.uuid))

    # TODO: does not work when period is before and after placed period: 2017-01-01 and 2019-01-01 when periods are in that period
    #
    # add new module location
    #
    Module_Location.create(module=module, location=location, start_date=_placed_on, end_date=_placed_til)

    return redirect(url_for('admin.module', module_uuid=module.uuid))


@admin.route('/module/new', methods=['POST'])
def new_module():
    type = Module_Type.select().where(Module_Type.id == request.form['module_type'])

    if not type.exists():
        flash('Module type bestaat niet.', AlertType.WARNING.value)
        return redirect(url_for('admin.modules'))

    module = Module(type=type)
    module.save()
    return redirect(url_for('admin.modules'))
1