from flask import Blueprint

# DO NOT IMPORT FROM HERE
# DO IT FROM routes.py
auth = Blueprint('auth', __name__, template_folder='templates')
