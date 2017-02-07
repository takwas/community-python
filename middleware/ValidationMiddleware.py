from functools import wraps
from flask import flash, redirect, url_for, jsonify
from helpers import validate
from helpers.enums import AlertType


def uuid_validation(json_response=False, redirect_url=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            for key, value in kwargs.items():
                if key.endswith('_uuid'):
                    if validate.uuid_validation(value):
                        return f(*args, **kwargs)
                    if json_response is True:
                        return jsonify({'error': 'invalid uuid'})
                    flash('Ongeldige UUID.', AlertType.WARNING.value)
                    return redirect(url_for(redirect_url))
        return decorated_function
    return decorator

