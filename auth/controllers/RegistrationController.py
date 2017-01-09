from ..blueprint import auth
from models import User
from flask import redirect, url_for
import bcrypt


@auth.route('/register')
def register():
    hashed = bcrypt.hashpw('test', bcrypt.gensalt())
    user = User(
        fname='Theo',
        sname='Bouwman',
        email='theobouwman98@gmail.com',
        password=hashed
    )
    user.save()
    return redirect(url_for('auth.login'))
