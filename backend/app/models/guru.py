from app.extensions import db
from app.models.base import BaseModel

class Guru(BaseModel):
    __tablename__ = 'guru'

    nip = db.Column(db.String(30), unique=True, index=True) # NIP bisa opsional bagi non-PNS, tapi kalau ada unique
    nuptk = db.Column(db.String(30), unique=True)
    nama_lengkap = db.Column(db.String(100), nullable=False)
    jenis_kelamin = db.Column(db.String(1)) # L/P
    tempat_lahir = db.Column(db.String(50))
    tanggal_lahir = db.Column(db.Date)
    agama = db.Column(db.String(20))
    alamat = db.Column(db.Text)
    no_hp = db.Column(db.String(20))
    status_aktif = db.Column(db.Boolean, default=True)

    # Relation to User (1 to 1)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    user = db.relationship('User', back_populates='guru')
    
    # Wali kelas
    rombel = db.relationship('Rombel', back_populates='wali_kelas')
    
    # Mengajar di Rombel
    mengajar = db.relationship('Mengajar', back_populates='guru')

    def __repr__(self):
        return f"<Guru {self.nama_lengkap}>"
