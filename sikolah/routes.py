from flask import render_template, url_for, flash, redirect, request
from flask_mail import Message
from sikolah import app, mail
from sikolah.forms import LoginForm
from sikolah.models import Siswa, Pelajaran, Nilai, User


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        if login_form.username.data == "admin" and login_form.password.data == "admin":
            flash(f"Selamat Datang Di Sikolah, {login_form.username.data}.", "success")
            return redirect(url_for("admin.index"))
        else:
            flash(f"Username atau password salah.", "error")
            return redirect(url_for("login"))

    return render_template("login.html", title="Login", form=login_form)


@app.route("/email")
def email():
    return render_template("email.html")


@app.route("/send_message", methods=["POST", "GET"])
def send_message():
    if request.method == "POST":
        email = request.form["email"]
        msg = f"Username dan Password anda adalah {email}, {request.form['message']}"
        subject = request.form["subject"]
        message = Message(subject, sender="lee.jadon.k@gmail.com", recipients=[email])
        message.body = msg
        mail.send(message)
        success = "Message sent"

        return "berhasil"