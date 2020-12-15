from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    BooleanField,
    SelectField,
    DateField,
)
from wtforms.validators import DataRequired, ValidationError, Email


class LoginForm(FlaskForm):
    username = StringField(
        "Username atau Email",
        validators=[DataRequired()],
        render_kw={"placeholder": "Username atau Email", "autofocus": "on"},
    )
    password = PasswordField(
        "Password", validators=[DataRequired()], render_kw={"placeholder": "Password"}
    )
    remember = BooleanField("Remember me")
    submit = SubmitField("Login")


class UpdateProfileForm(FlaskForm):
    nama = StringField(
        "Nama", validators=[DataRequired()], render_kw={"autofocus": "on"}
    )
    nis = StringField("NIM", validators=[DataRequired()], render_kw={"readonly": "on"})
    tempat_lahir = StringField("Tempat Lahir", validators=[DataRequired()])
    tanggal_lahir = DateField(
        "Tanggal Lahir",
        validators=[DataRequired()],
        render_kw={"placeholder": "format : yyyy-mm-dd"},
        format="%Y-%m-%d",
    )
    alamat = StringField("Alamat", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    gambar = FileField("Foto Profil", validators=[FileAllowed(["jpg", "png", "jpeg"])])
    submit = SubmitField("Edit Profil")


class EmailForm(FlaskForm):
    emails = SelectField("Pilih Alamat Email User :", choices=[])
    submit = SubmitField("Kirim Email")
