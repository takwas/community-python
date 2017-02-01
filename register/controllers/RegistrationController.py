from flask import request, render_template, redirect, url_for
from ..forms.register import SimpleRegistrationForm
from ..blueprint import register


@register.route('/', methods=['GET', 'POST'])
def index():
    form = SimpleRegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        return redirect(url_for('register.index'))
    return render_template('pages/home.html', form=form)