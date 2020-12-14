from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
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
    submit = SubmitField("Login")


class SendAccountForm(FlaskForm):
    pass
    # submit = SubmitField("Send Account")