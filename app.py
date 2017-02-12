from flask_celery import make_celery
from flask import Flask
from api.routes import api
from admin.routes import admin
from auth.routes import auth

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(api, url_prefix='/api')

app.testing = True

celery = make_celery(app)

import tasks.periodic
from tasks.mail import confirmation_mail

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    print(app.config['result_backend'])
