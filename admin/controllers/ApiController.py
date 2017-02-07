from flask import jsonify, make_response

from middleware import ValidationMiddleware
from models import Module_Location, Module
from ..blueprint import admin
from helpers import json, validate


@admin.route('/api/modules/module/<module_uuid>/locations')
@ValidationMiddleware.uuid_validation(json_response=True)
def api_module_locations(module_uuid):
    module = Module.select().where(Module.uuid == module_uuid)

    if not module.exists():
        resp = make_response(jsonify({'error': 'module not found.'}), 404)
        return resp

    module = module.get()

    module_locations = Module_Location.select().where(Module_Location.module == module)

    dict = json.models_to_dict(module_locations)

    for m in dict:
        m['start'] = m['start_date']
        m['end'] = m['end_date']
        m['title'] = m['location']['address'] + ', ' + m['location']['city']

    return jsonify(dict)