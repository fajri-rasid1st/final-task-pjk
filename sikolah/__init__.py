from flask import Flask
from flask_mail import Mail
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# app
app = Flask(__name__)

# app config
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/final_task"
app.config["SECRET_KEY"] = "c7de7e1c97f15fe"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# app mail config
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "lee.jadon.k@gmail.com"
app.config["MAIL_PASSWORD"] = "fwcydwxzbpsmeoqn"

# db
db = SQLAlchemy(app)

# migrate
migrate = Migrate(app, db)

# mail
mail = Mail(app)

# login manager
login_manager = LoginManager(app)
login_manager.login_view = "login"

from sikolah import routes
from sikolah.errors.handlers import errors

# register blue print
app.register_blueprint(errors)
