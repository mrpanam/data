import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail


def save_picture(form_picture):
    #gives a random name to the picture uploaded
    random_hex= secrets.token_hex(8)
    #get the name and extension of the picture uploaded
    f_name, f_ext = os.path.splitext(form_picture.filename)
    picture_fn=random_hex+f_ext
    picture_path=os.path.join(current_app.root_path,'static/profile',picture_fn)
    size=(125,125)
    i = Image.open(form_picture)
    i.thumbnail(size)
    i.save(picture_path)
    return picture_fn


def send_reset_email(user):
    token=user.get_reset_token()
    msg=Message('Password reset request', sender='ricoblog@demo.com', recipients=[user.email])

    msg.body = f'''To reset your password, visit the following link:
{url_for('reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)

