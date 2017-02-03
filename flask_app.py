from flask import Flask
from api.routes import api
from admin.routes import admin
from auth.routes import auth

app = Flask(__name__)
app.secret_key = 'RUSeFgS70r74pW144kmS83W3379eKkY3'

# TODO: db_name config everywhere
app.config['db_name'] = 'woodys_platform'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6Lfu5RMUAAAAAEyGL8PKaKfVho6iuUSGISdY6Si3'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6Lfu5RMUAAAAAK0bNT4mJgQgfw2oY1Z1Btn'
app.config['CELERY_BROKER_URL'] = 'amqp://localhost/'
app.config['CELERY_RESULT_BACKEND'] = 'db+postgresql://postgres@localhost/%s' % app.config.get('db_name')
app.config['email_email'] = 'noreply.platform.comunity@gmail.com'
app.config['email_password'] = 'derdure21'
app.config['email_host'] = 'smtp.gmail.com:587'

app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(api, url_prefix='/api')

app.testing = True
