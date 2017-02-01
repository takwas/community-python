from flask import Flask

from api.routes import api
from admin.routes import admin
from auth.routes import auth
from register.routes import register

app = Flask(__name__)
app.secret_key = 'RUSeFgS70r74pW144kmS83W3379eKkY3'

app.config['RECAPTCHA_PUBLIC_KEY'] = '6Lfu5RMUAAAAAEyGL8PKaKfVho6iuUSGISdY6Si3'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6Lfu5RMUAAAAAK0bNT4mJgQgfw2oY1Z1Btn'

app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(register, url_prefix='/register')


app.testing = True

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')