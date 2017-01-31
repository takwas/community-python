from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, PasswordField
import wtforms.validators as v



class SimpleRegistrationForm(FlaskForm):
    fname = StringField('Voornaam', [
        v.InputRequired(message='verplicht')])
    sname = StringField('Achternaam', [
        v.InputRequired(message='verplicht')])
    email = StringField('Email', [
        v.InputRequired(message='verplicht'),
        v.email(message='moet een geldig email zijn')])
    password = PasswordField('Wachtwoord', [
        v.InputRequired(message='verplicht'),
        v.EqualTo('password_check', message='wachtwoorden komen niet overeen')])
    password_check = PasswordField('Herhaal wachtwoord', [
        v.InputRequired(message='verplicht')])
    captcha = RecaptchaField()
    submit = SubmitField('Registreren')