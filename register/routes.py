from models import initialize_db, close_db_connection
from .blueprint import register
from flask import render_template, request
from .forms.register import SimpleRegistrationForm


@register.before_request
def before_request():
    initialize_db()


@register.teardown_request
def teardown_request(exception):
    close_db_connection()

@register.route('/')
def index():
    form = SimpleRegistrationForm(request.form)
    return render_template('pages/home.html', form=form)