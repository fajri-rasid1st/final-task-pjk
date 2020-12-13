from sikolah import db, admin
from flask_admin.contrib.sqla import ModelView


class Siswa(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nis = db.Column(db.String(10), unique=True, nullable=False)
    nama = db.Column(db.String(60), nullable=False)
    tempat_lahir = db.Column(db.String(30), nullable=False)
    tanggal_lahir = db.Column(db.Date, nullable=False)
    alamat = db.Column(db.String(100), nullable=False)
    pelajaran = db.relationship("Pelajaran", backref="data_pelajaran", lazy=True)
    nilai = db.relationship("Nilai", backref="data_nilai", lazy=True)
    user = db.relationship("User", backref="data_user", lazy=True)

    def __repr__(self):
        return f"Siswa('{self.nama}', '{self.nis}')"

    def _asdict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}


class Pelajaran(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nama_pelajaran = db.Column(db.String(50), nullable=False)
    id_siswa = db.Column(db.Integer, db.ForeignKey("siswa.id"), nullable=False)

    def __repr__(self):
        return f"Pelajaran('{self.nama_pelajaran}')"

    def _asdict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}


class Nilai(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    nilai = db.Column(db.Numeric(5, 2), nullable=False)
    id_siswa = db.Column(db.Integer, db.ForeignKey("siswa.id"), nullable=False)
    id_pelajar = db.Column(db.Integer, db.ForeignKey("pelajaran.id"), nullable=False)

    def __repr__(self):
        return f"Nilai('{self.id_siswa}', '{self.id_pelajar}', '{self.semester}', '{self.nilai}')"

    def _asdict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_name = db.Column(db.String(50), nullable=False)
    passsword = db.Column(db.String(128), nullable=False)
    hak_akses = db.Column(db.String(10), nullable=False)
    id_siswa = db.Column(db.Integer, db.ForeignKey("siswa.id"), nullable=False)

    def __repr__(self):
        return f"User('{self.user_name}','{self.passsword}','{self.hak_akses}', '{self.id_siswa}')"

    def _asdict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}


admin.add_view(ModelView(Siswa, db.session))
admin.add_view(ModelView(Pelajaran, db.session))
admin.add_view(ModelView(Nilai, db.session))
admin.add_view(ModelView(User, db.session))
