import bcrypt
from flask import request, render_template, redirect, url_for, flash
from ..forms.register import SimpleRegistrationForm
from ..blueprint import register
from models import User, User_Role


@register.route('/', methods=['GET', 'POST'])
def index():
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
            return redirect(url_for('register.index'))

        user = User(fname=fname, sname=sname, email=email, password=hashed)
        user.save()

        flash('Uw account is aangemaakt. Kijk in uw mailbox voor de activatie link')
        return redirect(url_for('register.index'))
    return render_template('pages/home.html', form=form)