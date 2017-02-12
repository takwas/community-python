from app import celery, app
from models import User
from mailer_jinja2.mail import Mail
from smtplib import SMTP
from flask import url_for


@celery.task(name='mail.confirmation_mail')
def confirmation_mail(user_id: int):
    with app.app_context():
        u = User.get(User.id == user_id)

        server = SMTP(app.config.get('EMAIL_HOST'))
        server.ehlo()
        server.starttls()
        server.login(app.config.get('EMAIL_EMAIL'), app.config.get('EMAIL_PASSWORD'))

        website_name = app.config.get('WEBSITE_NAME')
        url = url_for('auth.activate', user_uuid=u.uuid, activation_key=u.activation_key)
        activation_link = url

        mail = Mail(from_address=app.config.get('EMAIL_EMAIL'),
                    to_address=u.email,
                    subject='Account activatie %s' % website_name,
                    template='templates/mail/confirmation_mail.html',
                    server=server,
                    user=u,
                    website_name=website_name,
                    activation_link=activation_link)
        mail.send_message()
