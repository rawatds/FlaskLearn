from flask import  url_for
from blog import app, mail

import secrets
import os
from PIL import Image
import pytz
from dateutil.tz import tzlocal
from flask_mail import Message


def date_format(mydate):
    mydate = mydate.replace(tzinfo=pytz.UTC)

    # Convert UTC to localtimezone, and then format it
    mydate = mydate.replace(tzinfo=pytz.UTC)

    #return mydate.astimezone(pytz.timezone('UTC')).astimezone(tzlocal()).strftime('%d %b, %Y at %H:%M')
    #return mydate.tz=pytz.UTC).astimezone(tzlocal()).strftime('%d %b, %Y at %H:%M')
    return mydate.astimezone(tzlocal()).strftime('%d %b, %Y at %H:%M')


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, fext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + fext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    output_size = (250, 250)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    #form_picture.save(picture_path)
    i.save(picture_path)
    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()

    msg = Message('Blog - Password reset request', sender='dsrawat.temp@gmail.com', recipients=[user.email])
    msg.html = f"""<p>To reset your password, visit the link below</p> <br>

    <a href='{url_for('users_bp.reset_token', token=token, _external=True)}'>
        {url_for('users_bp.reset_token', token=token, _external=True)}
    </a>
    <br/><br/>
    If you did not made this request, please ignore this email and no change will be done. <br/><br/>
    -- Admin, MyBlog
"""
    mail.send(msg)
