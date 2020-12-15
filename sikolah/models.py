from flask import url_for, redirect, abort
from flask_login import UserMixin, current_user
from flask_admin import Admin, BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from sikolah import app, db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Siswa(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nis = db.Column(db.String(10), unique=True, nullable=False)
    nama = db.Column(db.String(60), nullable=False)
    tempat_lahir = db.Column(db.String(30), nullable=False)
    tanggal_lahir = db.Column(db.Date, nullable=False)
    alamat = db.Column(db.String(100), nullable=False)
    gambar = db.Column(db.String(255), nullable=False, default="default.jpg")
    email = db.Column(db.String(255), unique=True, nullable=False)
    user = db.relationship("User", backref="data_siswa", lazy=True)

    def __repr__(self):
        return f"Siswa('{self.nama}', '{self.nis}')"

    def __asdict(self):
        return {c.name: str(getattr(self, c.name)) for c in self._table_.columns}


class Pelajaran(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nama_pelajaran = db.Column(db.String(50), nullable=False)
    nilai = db.relationship("Nilai", backref="data_pelajaran_siswa", lazy=True)

    def __repr__(self):
        return f"Pelajaran('{self.nama_pelajaran}')"

    def __asdict(self):
        return {c.name: str(getattr(self, c.name)) for c in self._table_.columns}


class Nilai(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    nilai = db.Column(db.Numeric(5, 2), nullable=False)
    id_siswa = db.Column(db.Integer, db.ForeignKey("siswa.id"), nullable=False)
    id_pelajar = db.Column(db.Integer, db.ForeignKey("pelajaran.id"), nullable=False)
    nilai_siswa = db.relationship("Siswa", backref="data_nilai_siswa", lazy=True)

    def __repr__(self):
        return f"Nilai('{self.id_siswa}', '{self.id_pelajar}', '{self.semester}', '{self.nilai}')"

    def __asdict(self):
        return {c.name: str(getattr(self, c.name)) for c in self._table_.columns}


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    hak_akses = db.Column(db.String(10), nullable=False)
    id_siswa = db.Column(db.Integer, db.ForeignKey("siswa.id"))

    def __repr__(self):
        return f"User('{self.user_name}','{self.password}','{self.hak_akses}', '{self.id_siswa}')"

    def __asdict(self):
        return {c.name: str(getattr(self, c.name)) for c in self._table_.columns}


class MyModelView(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated:
            if current_user.hak_akses == "siswa":
                return False
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return abort(404)


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        if current_user.is_authenticated:
            if current_user.hak_akses == "siswa":
                return False
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return abort(404)


# admin
admin = Admin(app, template_mode="bootstrap4", index_view=MyAdminIndexView())

admin.add_view(MyModelView(Siswa, db.session))
admin.add_view(MyModelView(Pelajaran, db.session))
admin.add_view(MyModelView(Nilai, db.session))
admin.add_view(MyModelView(User, db.session))