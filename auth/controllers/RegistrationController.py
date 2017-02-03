from ..blueprint import auth
from models import User
from flask import redirect, url_for, request, render_template, flash
import bcrypt
from ..forms.register import SimpleRegistrationForm
from tasks.add import add


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = SimpleRegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        fname = request.form['fname']
        sname = request.form['sname']
        email = request.form['email']
        password = request.form['password']
        hashed = bcrypt.hashpw(password.encode('utf-8 '), bcrypt.gensalt())

        user = User.select().where(User.email == email)
        if user.exists():
            flash('Er bestaat al een account met dit email adres')
            return redirect(url_for('auth.register'))

        user = User(fname=fname, sname=sname, email=email, password=hashed)
        user.save()

        flash('Uw account is aangemaakt. Kijk in uw mailbox voor de activatie link')
        return redirect(url_for('auth.register'))
    return render_template('pages/register.html', form=form)


@auth.route('/register/test')
def register_test():
    add.delay()
    # hashed = bcrypt.hashpw('test'.encode('utf-8 '), bcrypt.gensalt())
    # user = User(
    #     fname='Theo',
    #     sname='Bouwman',
    #     email='theobouwman98@gmail.com',
    #     password=hashed
    # )
    # user.save()
    return redirect(url_for('auth.login'))
