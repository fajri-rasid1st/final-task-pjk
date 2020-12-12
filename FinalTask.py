from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin, BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/final_task"
app.config["SECRET_KEY"] = "c7de7e1c97f15fe"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
admin = Admin(app)

class Siswa(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nis = db.Column(db.String(10), unique=True, nullable=False)
    nama = db.Column(db.String(60), nullable=False)
    tempat_lahir = db.Column(db.String(30), nullable=False)
    tanggal_lahir = db.Column(db.Date, nullable=False)
    alamat = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"Siswa('{self.nama}', '{self.nis}')"

    def _asdict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}


class Pelajaran(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nama_pelajaran = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Pelajaran('{self.nama_pelajaran}')"

    def _asdict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}


class Nilai(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    id_siswa = db.Column(db.Integer, db.ForeignKey("siswa.id"), nullable=False)
    id_pelajar = db.Column(db.Integer, db.ForeignKey("pelajaran.id"), nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    nilai = db.Column(db.Numeric(5, 2), nullable=False)

    siswa = db.relationship('Siswa', backref=db.backref('data_siswa'))
    pelajaran = db.relationship('Pelajaran', backref=db.backref('data_pelajaran'))

    def __repr__(self):
        return f"Nilai('{self.id_siswa}', '{self.id_pelajar}', '{self.semester}', '{self.nilai}')"

    def _asdict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_name = db.Column(db.String(50), db.ForeignKey('siswa.email'), unique=True, nullable=False)
    passsword = db.Column(db.String(128), nullable=False)
    hak_akses = db.Column(db.String(10), nullable=False)

    email = db.relationship('Siswa', backref=db.backref('user_email'), uselist=False)
    
    def __repr__(self):
        return f"User('{self.user_name}','{self.passsword}','{self.hak_akses}')"

    def _asdict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}


admin.add_view(ModelView(Siswa, db.session))
admin.add_view(ModelView(Pelajaran, db.session))
admin.add_view(ModelView(Nilai, db.session))
admin.add_view(ModelView(User, db.session))


@app.route("/")
def index():
    return "under construction"


if __name__ == "__main__":
    app.run(debug=True)
