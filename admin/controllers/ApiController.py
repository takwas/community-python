from flask import jsonify, make_response
from models import Module_Location, Module
from ..blueprint import admin
from helpers.json import models_to_dict

@admin.route('/api/modules/module/<module_id>/locations')
def api_module_locations(module_id):
    module = Module.select().where(Module.id == module_id)

    if not module.exists():
        resp = make_response(jsonify({'error': 'module not found.'}), 404)
        return resp

    module = module.get()

    module_locations = Module_Location.select().where(Module_Location.module == module)

    dict = models_to_dict(module_locations)

    for m in dict:
        m['start'] = m['start_date']
        m['end'] = m['end_date']
        m['title'] = m['location']['address'] + ', ' + m['location']['city']
        m['allDay'] = True

    return jsonify(dict)