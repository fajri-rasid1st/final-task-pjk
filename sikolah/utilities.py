from flask import current_app, redirect, url_for
from flask_mail import Message
from sikolah import mail
from PIL import Image
import secrets
import os


def save_picture(form_pict):
    # generate random string
    rand_hex = secrets.token_hex(8)
    # split name of file and extension
    _, file_ext = os.path.splitext(form_pict.filename)
    # create new file name
    file_name = rand_hex + file_ext
    # path where file will be saved
    file_path = os.path.join(current_app.root_path, "static/img", file_name)
    # resize the image
    img = Image.open(form_pict)
    img.thumbnail((250, 250))
    # save picture
    img.save(file_path)
    # return picture name
    return file_name


def send_message(user):
    message = Message(
        subject="[Account User | Sikolah]",
        sender="lee.jadon.k@gmail.com",
        recipients=[user.data_siswa.email],
    )
    message.html = f"""
        <h1> Halo, {user.data_siswa.nama}. </h1>
        <p> Berikut adalah username dan password "Sikolah" anda: </p>
        <table style="font-weight: 500;">
            <tr>
                <td>Username/Email</td>
                <td> : {user.user_name}</td>
            </tr>
            <tr>
                <td>Password</td>
                <td> : {user.password}</td>
            </tr>
        </table>
        <br />
        <p> Harap agar menjaga password anda agar tetap aman! </p>
    """
    mail.send(message)

    return redirect(url_for("email"))