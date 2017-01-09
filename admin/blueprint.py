from flask import Blueprint

# DO NOT IMPORT FROM HERE
# DO IT FROM routes.py
admin = Blueprint(
    'admin', __name__,
    template_folder='templates',
    static_folder='static'
)
