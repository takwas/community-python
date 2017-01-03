from flask import Flask

from api.routes import api
from admin.routes import admin
from auth.routes import auth

app = Flask(__name__)
app.secret_key = 'community_secret_key'

app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(auth, url_prefix='/auth')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
