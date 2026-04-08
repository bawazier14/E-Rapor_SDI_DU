from app.extensions import db
from app.models.base import BaseModel

class Rombel(BaseModel):
    __tablename__ = 'rombel'

    nama = db.Column(db.String(50), nullable=False) # e.g. 1A, 1B, 2A
    tahun_ajaran_id = db.Column(db.Integer, db.ForeignKey('tahun_ajaran.id'), nullable=False)
    kelas_id = db.Column(db.Integer, db.ForeignKey('kelas.id'), nullable=False)
    wali_kelas_id = db.Column(db.Integer, db.ForeignKey('guru.id')) # Optional at creation
    
    tahun_ajaran = db.relationship('TahunAjaran', back_populates='rombels')
    kelas = db.relationship('Kelas', back_populates='rombels')
    wali_kelas = db.relationship('Guru', back_populates='rombel')
    
    # Students in this rombel
    siswas = db.relationship('Siswa', secondary='anggota_rombel', back_populates='rombels')

    # Mengajar setup
    mengajar = db.relationship('Mengajar', back_populates='rombel')

    # Transaksi
    absensi = db.relationship('Absensi', back_populates='rombel')
    
    def __repr__(self):
        return f"<Rombel {self.nama}>"
