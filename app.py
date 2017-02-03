from flask import Flask
from flask_celery import make_celery
from api.routes import api
from admin.routes import admin
from auth.routes import auth
from tasks import add

app = Flask(__name__)
app.secret_key = 'RUSeFgS70r74pW144kmS83W3379eKkY3'

# TODO: db_name config everywhere
app.config['db_name'] = 'woodys_platform'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6Lfu5RMUAAAAAEyGL8PKaKfVho6iuUSGISdY6Si3'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6Lfu5RMUAAAAAK0bNT4mJgQgfw2oY1Z1Btn'
app.config['CELERY_BROKER_URL'] = 'amqp://localhost/'
app.config['CELERY_RESULT_BACKEND'] = 'db+postgresql://postgres@localhost/%s' % app.config.get('db_name')

app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(api, url_prefix='/api')

celery = make_celery(app)


@app.route('/task')
def task():
    add.add_together.delay(10, 15)
    return 'task started'


app.testing = True

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
