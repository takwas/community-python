from peewee import SelectQuery
from playhouse.shortcuts import model_to_dict
from ..blueprint import auth
from models import User
from flask import redirect, url_for, request, render_template, flash, session
import bcrypt
from ..forms.register import SimpleRegistrationForm


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

        user = User.create(fname=fname, sname=sname, email=email, password=hashed)

        user_dict = model_to_dict(user, fields_from_query=SelectQuery(User, User.uuid, User.fname, User.sname,
                                                                      User.email, User.activation_key))

        # Trigger confirmation mail tast
        from tasks.mail.confirmation_mail import confirmation_mail
        confirmation_mail.delay(user_dict)

        flash('Uw account is aangemaakt. Kijk in uw mailbox voor de activatie link')
        return redirect(url_for('auth.register'))
    return render_template('pages/register.html', form=form)


@auth.route('/register/test')
def register_test():

    # print(session['user'])
    #
    # u = User.from_object(session['user'])
    #
    # from tasks.mail.confirmation_mail import confirmation_mail
    # confirmation_mail.delay(model_to_dict(u))
    hashed = bcrypt.hashpw('test'.encode('utf-8 '), bcrypt.gensalt())
    user = User(
        fname='Theo',
        sname='Bouwman',
        email='theobouwman98@gmail.com',
        password=hashed
    )
    user.save()
    return 1
