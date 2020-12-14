from flask import render_template, url_for, flash, redirect, request
from flask_mail import Message
from flask_login import login_user, login_required, current_user, logout_user
from sikolah import app, mail
from sikolah.forms import LoginForm
from sikolah.models import Siswa, Pelajaran, Nilai, User
import datetime


@app.route("/")
@app.route("/home")
@login_required
def home():
    return render_template("home.html", title="Home")


@app.route("/about")
@login_required
def about():
    return render_template("about.html", title="About")


@app.route("/login", methods=["GET", "POST"])
def login():
    # check if user is already log in
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    # declarate class LoginForm
    login_form = LoginForm()
    # when user click the submit button
    if login_form.validate_on_submit():
        # check user if exist on database
        user = User.query.filter_by(user_name=login_form.username.data).first()
        # if user is found in databse
        if user and user.password == login_form.password.data:
            # login
            login_user(
                user=user,
                remember=login_form.remember.data,
                duration=datetime.timedelta(seconds=8000),
            )
            # flash message when login success
            flash(f"Selamat datang di sikolah, {user.user_name}!", "success")
            next_page = request.args.get("next")

            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            # flash message when login failed
            flash(f"Username atau password salah.", "error")

    return render_template("login.html", title="Login", form=login_form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/email")
@login_required
def email():
    return render_template("email.html", title="Send Email")


@app.route("/send_message", methods=["POST", "GET"])
@login_required
def send_message():
    if request.method == "POST":
        email = request.form["email"]
        msg = f"Username dan Password anda adalah {email}, {request.form['message']}"
        subject = request.form["subject"]
        message = Message(subject, sender="lee.jadon.k@gmail.com", recipients=[email])
        message.body = msg
        mail.send(message)
        return redirect(url_for("admin.email"))


@app.route("/scores")
@login_required
def scores():
    course_list = []

    for i in list(User.query.get(1).data_siswa.data_nilai_siswa):
        course_list.append([i.semester, i])

    sorted_course_list = sorted(course_list, key=lambda index: index[0])

    return render_template(
        "scores.html",
        title="Nilai Siswa",
        data_nilai=[i[1] for i in sorted_course_list],
        data_siswa=User.query.get(1).data_siswa,
    )
