from functools import wraps

import jwt
from flask import url_for, redirect, session, request, make_response, jsonify, current_app, flash
from playhouse.shortcuts import dict_to_model

from helpers.enums.auth import AuthRoleType
from models import Role


def login_required(f):
    """
    ONLY USE FOR GENERIC PURPOSES
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session is not None:
            if 'user' not in session:
                flash('Hiervoor moet u ingelogd zijn')
                return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function


def admin_role_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session is not None:
            if 'user' in session and 'active_role' in session:
                actr = dict_to_model(data=session['active_role'], model_class=Role)
                if actr.role == AuthRoleType.ADMIN.value:
                    return f(*args, **kwargs)
        flash('Voor deze actie moet u een administrator zijn')
        return redirect(url_for('auth.login'))
    return decorated_function


def no_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session is not None:
            if 'user' in session and 'active_role' in session:
                return redirect(url_for('auth.logout'))
        return f(*args, **kwargs)
    return decorated_function


def token_verification(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')

        # check for auth header
        if auth_header is None:
            resp = make_response(jsonify({'error': 'No Authorization header found'}), 403)
            return resp

        try:
            # try to decode token
            current_user = jwt.decode(auth_header, current_app.secret_key)
            # add current user to request.current_user
            request.current_user = current_user
        except:
            resp = make_response(jsonify({'error': 'Invalid Authorization token'}), 403)
            return resp

        return f(*args, **kwargs)
    return decorated_function