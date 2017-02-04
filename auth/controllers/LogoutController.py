from flask import redirect, session, url_for, flash
from middleware import AuthMiddleware
from ..blueprint import auth


@auth.route('/logout')
@AuthMiddleware.login_required
def logout():
    session.pop('user', None)
    session.pop('active_role', None)
    flash('U bent succesvol uitgelogd', AlertType.WARNING.value)
    return redirect(url_for('auth.login'))
