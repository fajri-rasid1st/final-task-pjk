from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, DateField
from wtforms.validators import DataRequired, ValidationError


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
    # nama = StringField('Nama', validators=[DataRequired()], render_kw={'autofocus': 'on'})
    tempat_lahir = StringField('Tempat Lahir', validators=[DataRequired()], render_kw={"autofocus": "on"})
    tanggal_lahir = DateField('Tanggal Lahir', validators=[DataRequired()] , format='%Y-%m-%d')
    alamat = StringField('Alamat', validators=[DataRequired()])


class SendAccountForm(FlaskForm):
    # submit = SubmitField("Send Account")
    pass


# class SelectSemesterForm(FlaskForm):
#     options = SelectField(
#         u"Pilih Semester",
#         choices=[("1", "Semester 1"), ("2", "Semester 2"), ("3", "Semester 3")],
#     )
#     submit = SubmitField("Submit")