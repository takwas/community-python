from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class SimpleRegistrationForm(FlaskForm):
    fname = StringField('Voornaam', validators=[DataRequired()])
    sname = StringField('Achternaam', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])