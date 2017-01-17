from flask import Blueprint

# DO NOT IMPORT FROM HERE
# DO IT FROM routes.py
register = Blueprint(
    'register', __name__,
    template_folder='templates',
    static_folder='static'
)
