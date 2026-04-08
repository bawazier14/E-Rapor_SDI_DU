from app.extensions import db
from app.models.base import BaseModel

# Association table for Romble to Siswa (Many-to-Many if history is kept in Romble)
# OR Siswa BelongsTo Rombel (One-to-Many).
# In an academic system, a Siswa is enrolled in a specific Rombel per semester.
class AnggotaRombel(BaseModel):
    __tablename__ = 'anggota_rombel'
    
    rombel_id = db.Column(db.Integer, db.ForeignKey('rombel.id'), nullable=False)
    siswa_id = db.Column(db.Integer, db.ForeignKey('siswa.id'), nullable=False)
    
    # Optional fields for student's specific status in this rombel (e.g., active, pindah)
    status = db.Column(db.String(20), default='aktif')

class Siswa(BaseModel):
    __tablename__ = 'siswa'

    nisn = db.Column(db.String(20), unique=True, index=True)
    nis = db.Column(db.String(20), unique=True, index=True)
    nama_lengkap = db.Column(db.String(100), nullable=False)
    jenis_kelamin = db.Column(db.String(1)) # L/P
    tempat_lahir = db.Column(db.String(50))
    tanggal_lahir = db.Column(db.Date)
    agama = db.Column(db.String(20))
    alamat = db.Column(db.Text)
    nama_ayah = db.Column(db.String(100))
    nama_ibu = db.Column(db.String(100))
    pekerjaan_ayah = db.Column(db.String(50))
    pekerjaan_ibu = db.Column(db.String(50))
    alamat_orang_tua = db.Column(db.Text)
    no_hp_orang_tua = db.Column(db.String(20))
    status_aktif = db.Column(db.String(20), default='aktif') # aktif, lulus, pindah, keluar

    # Relation to User (1 to 1) - Optional for parent/student portal
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=True)
    user = db.relationship('User', back_populates='siswa')

    # Anggota Rombel (History of classes)
    rombels = db.relationship('Rombel', secondary='anggota_rombel', back_populates='siswas')
    
    # Nilai, Absensi, etc
    nilai = db.relationship('Nilai', back_populates='siswa')
    absensi = db.relationship('Absensi', back_populates='siswa')
    ekskul = db.relationship('NilaiEkskul', back_populates='siswa')
    catatan = db.relationship('CatatanWaliKelas', back_populates='siswa')
    rapor = db.relationship('Rapor', back_populates='siswa')

    def __repr__(self):
        return f"<Siswa {self.nama_lengkap}>"
