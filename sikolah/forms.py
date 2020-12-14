from flask_wtf import FlaskForm
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
        "Username or Email",
        validators=[DataRequired()],
        render_kw={"placeholder": "Username", "autofocus": "on"},
    )
    password = PasswordField(
        "Password", validators=[DataRequired()], render_kw={"placeholder": "Password"}
    )
    remember = BooleanField("Remember me")
    submit = SubmitField("Login")


class UpdateProfileForm(FlaskForm):
    tempat_lahir = StringField(
        "Tempat Lahir", validators=[DataRequired()], render_kw={"autofocus": "on"}
    )
    tanggal_lahir = DateField(
        "Tanggal Lahir", validators=[DataRequired()], format="%Y-%m-%d"
    )
    alamat = StringField("Alamat", validators=[DataRequired()])
    submit = SubmitField("Edit Profil")


class EmailForm(FlaskForm):
    emails = SelectField("Select Email Address :", choices=[])
    submit = SubmitField("Send Email")