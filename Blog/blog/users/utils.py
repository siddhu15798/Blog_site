import os
import secrets
from PIL import Image
from flask import url_for
from blog import app, mail
from flask_mail import Message

def save_pic(form_pic):
    random_hex = secrets.token_hex(8)
    _, file_ext = os.path.splitext(form_pic.filename)
    pic_fn = random_hex + file_ext
    pic_path = os.path.join(app.root_path, 'static/profile_pics', pic_fn)
    output_size = (125, 125)
    i = Image.open(form_pic)
    i.thumbnail(output_size)
    i.save(pic_path)
    return pic_fn

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='siddhu.15798@gmail.com', recipients=[user.email])
    msg.body = f'''To reset your password visit the following link: 
{url_for('users.reset_token', token=token, _external=True)}
If you did not make this request them simply ignore this message and no changes will be made.'''
    mail.send(msg)