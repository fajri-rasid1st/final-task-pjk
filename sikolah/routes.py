from flask import render_template, url_for, flash, redirect, request, abort, current_app
from flask_mail import Message
from flask_login import login_user, login_required, current_user, logout_user
from sikolah import app, mail, db
from sikolah.forms import LoginForm, EmailForm, UpdateProfileForm
from sikolah.models import Siswa, Pelajaran, Nilai, User
from sikolah.utilities import save_picture, send_message
import datetime


@app.route("/")
@app.route("/home")
@login_required
def home():
    file_gambar = url_for("static", filename=f"img/{current_user.data_siswa.gambar}")
    return render_template("home.html", title="Home", gambar=file_gambar)


@app.route("/about")
@login_required
def about():
    file_gambar = url_for("static", filename=f"img/{current_user.data_siswa.gambar}")
    return render_template("about.html", title="About", gambar=file_gambar)


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
            # login proccess
            login_user(
                user=user,
                remember=login_form.remember.data,
                duration=datetime.timedelta(seconds=600),
            )
            # flash message when login success
            flash(f"Selamat datang di sikolah, {user.data_siswa.nama}.", "success")
            # determine next page if exist
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


@app.route("/admin/email", methods=["GET", "POST"])
@login_required
def email():
    # check role of user
    if current_user.hak_akses != "admin":
        return abort(404)

    email_form = EmailForm()

    email_form.emails.choices = [
        (siswa.email) for siswa in Siswa.query.all() if siswa.nama.lower() != "admin"
    ]

    if email_form.validate_on_submit():
        user = User.query.filter_by(user_name=email_form.emails.data).first()
        send_message(user)
        flash("Pengiriman email sedang dalam proses.", "info")

    return render_template("email.html", title="Send Email", form=email_form)


@app.route("/scores", methods=["GET", "POST"])
@login_required
def scores():
    # check role of user
    if current_user.hak_akses != "siswa":
        return abort(404)

    file_gambar = url_for("static", filename=f"img/{current_user.data_siswa.gambar}")

    if request.method == "POST":
        selected_semester = request.form.get("select_semester")

        if selected_semester == "Pilih Semester":
            return redirect("scores")
        else:
            return redirect(f"scores/{selected_semester}")

    else:
        course_list = []

        for i in list(current_user.data_siswa.data_nilai_siswa):
            course_list.append([i.semester, i])

        sorted_course_list = sorted(course_list, key=lambda index: index[0])
        max_semester = [i[0] for i in sorted_course_list]

        return render_template(
            "scores.html",
            title="Nilai Siswa",
            data_nilai=[i[1] for i in sorted_course_list],
            data_semester=max_semester[len(max_semester) - 1],
            data_siswa=current_user.data_siswa,
            gambar=file_gambar,
        )


@app.route("/scores/<int:semester>")
@login_required
def scores_semester(semester):
    # check role of user
    if current_user.hak_akses != "siswa":
        return abort(404)

    file_gambar = url_for("static", filename=f"img/{current_user.data_siswa.gambar}")
    course_list = []

    for i in list(current_user.data_siswa.data_nilai_siswa):
        course_list.append([i.semester, i])

    sorted_course_list = sorted(course_list, key=lambda index: index[0])
    max_semester = [i[0] for i in sorted_course_list]
    selected_semester = []

    for i in sorted_course_list:
        if i[0] == semester:
            selected_semester.append(i[1])

    return render_template(
        "scores.html",
        title="Nilai Siswa",
        data_nilai=selected_semester,
        data_semester=max_semester[len(max_semester) - 1],
        data_siswa=current_user.data_siswa,
        gambar=file_gambar,
    )


@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    update_profil_form = UpdateProfileForm()

    if update_profil_form.validate_on_submit():
        if update_profil_form.gambar.data:
            simpan_gambar = save_picture(update_profil_form.gambar.data)
            current_user.data_siswa.gambar = simpan_gambar

        current_user.data_siswa.nama = update_profil_form.nama.data
        current_user.data_siswa.nis = update_profil_form.nis.data
        current_user.data_siswa.tempat_lahir = update_profil_form.tempat_lahir.data
        current_user.data_siswa.tanggal_lahir = update_profil_form.tanggal_lahir.data
        current_user.data_siswa.alamat = update_profil_form.alamat.data
        current_user.data_siswa.email = update_profil_form.email.data

        db.session.commit()
        flash("Berhasil mengedit profile.", "success")

        return redirect(url_for("profile"))

    elif request.method == "GET":
        update_profil_form.nama.data = current_user.data_siswa.nama
        update_profil_form.nis.data = current_user.data_siswa.nis
        update_profil_form.tempat_lahir.data = current_user.data_siswa.tempat_lahir
        update_profil_form.tanggal_lahir.data = current_user.data_siswa.tanggal_lahir
        update_profil_form.alamat.data = current_user.data_siswa.alamat
        update_profil_form.email.data = current_user.data_siswa.email
        update_profil_form.gambar.data = current_user.data_siswa.gambar

    else:
        flash("Gagal mengedit profile.", "error")

    file_gambar = url_for("static", filename=f"img/{current_user.data_siswa.gambar}")

    return render_template(
        "user_info.html",
        title="Profil",
        data=current_user.data_siswa,
        form=update_profil_form,
        gambar=file_gambar,
    )