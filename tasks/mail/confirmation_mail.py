from typing import Dict
from app import celery, app
from models import User
from mailer_jinja2.mail import Mail
from smtplib import SMTP


@celery.task(name='mail.confirmation_mail')
def confirmation_mail(user: Dict):
    with app.app_context():
        u = User.from_object(user)
        server = SMTP(app.config.get('email_host'))
        server.ehlo()
        server.starttls()
        server.login(app.config.get('email_email'), app.config.get('email_password'))

        website_name = 'Community'
        activation_link = app.config.get('website_link') + '/auth/activate/' + u.uuid + '/' + u.activation_key

        mail = Mail(from_address=app.config.get('email_email'),
                    to_address=u.email,
                    subject='Account activatie %s' % website_name,
                    template='templates/mail/confirmation_mail.html',
                    server=server,
                    user=u,
                    website_name=website_name,
                    activation_link=activation_link)
        mail.send_message()
