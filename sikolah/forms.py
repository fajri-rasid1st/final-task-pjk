from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
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


class EmailForm(FlaskForm):
    emails = SelectField("Select Email Address :", choices=[])
    submit = SubmitField("Send Email")


class UpdateForm(FlaskForm):
    pass
