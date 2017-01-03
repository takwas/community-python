from flask import url_for, redirect, request, session
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print(session is not None)
        if session is not None:
            if 'user' not in session:
                return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function
