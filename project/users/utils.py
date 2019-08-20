import os
import secrets
from flask import url_for, current_app
from flask_mail import Message
from app import mail 

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='noreply@gmail.com', recepients=[user.email])
    msg.body = f'''To Reset your password Visit the following link:
{url_for('users.reset_token', token=token, external=True)}
If you did not make this request simply ignore this email and no change will be effected
    '''
    mail.send(msg)
