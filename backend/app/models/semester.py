from app.extensions import db
from app.models.base import BaseModel

class Semester(BaseModel):
    __tablename__ = 'semester'

    tahun_ajaran_id = db.Column(db.Integer, db.ForeignKey('tahun_ajaran.id'), nullable=False)
    nama = db.Column(db.String(20), nullable=False) # Ganjil / Genap
    status_aktif = db.Column(db.Boolean, default=False)

    tahun_ajaran = db.relationship('TahunAjaran', back_populates='semesters')
    
    # Nilai, Absensi per semester
    nilai = db.relationship('Nilai', back_populates='semester')
    absensi = db.relationship('Absensi', back_populates='semester')
    ekskul = db.relationship('NilaiEkskul', back_populates='semester')
    catatan = db.relationship('CatatanWaliKelas', back_populates='semester')
    rapor = db.relationship('Rapor', back_populates='semester')

    def __repr__(self):
        return f"<Semester {self.nama}>"
