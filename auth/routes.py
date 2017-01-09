from flask import Blueprint, render_template, redirect, url_for, request, flash, session, jsonify, make_response, current_app
from playhouse.shortcuts import model_to_dict
from models import initialize_db, close_db_connection, User
import bcrypt
import datetime
import jwt
from blueprint import auth
from controllers import RegistrationController, AuthenticationController


@auth.before_request
def before_request():
    initialize_db()


@auth.teardown_request
def teardown_request(exception):
    close_db_connection()


@auth.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('auth.login'))
