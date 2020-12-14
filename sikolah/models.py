from sikolah import db, login_manager, admin
from flask_login import UserMixin
from flask_admin.contrib.sqla import ModelView


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
    id_siswa = db.Column(db.Integer, db.ForeignKey("siswa.id"), nullable=False)

    def __repr__(self):
        return f"User('{self.user_name}','{self.password}','{self.hak_akses}', '{self.id_siswa}')"

    def __asdict(self):
        return {c.name: str(getattr(self, c.name)) for c in self._table_.columns}


admin.add_view(ModelView(Siswa, db.session))
admin.add_view(ModelView(Pelajaran, db.session))
admin.add_view(ModelView(Nilai, db.session))
admin.add_view(ModelView(User, db.session))
