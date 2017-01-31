from flask import url_for, redirect, session, request, make_response, jsonify, current_app
from functools import wraps
import jwt


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session is not None:
            if 'user' not in session:
                return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function


def no_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session is not None:
            if 'user' in session:
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