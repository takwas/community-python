from flask_celery import make_celery
from flask_app import app

celery = make_celery(app)

from tasks import add

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
