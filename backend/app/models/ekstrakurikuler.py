from app.extensions import db
from app.models.base import BaseModel

class JenisEkskul(BaseModel):
    __tablename__ = 'jenis_ekskul'
    nama = db.Column(db.String(100), nullable=False)
    keterangan = db.Column(db.Text)
    
    nilai_ekskul = db.relationship('NilaiEkskul', back_populates='ekskul')

class NilaiEkskul(BaseModel):
    __tablename__ = 'nilai_ekskul'
    
    siswa_id = db.Column(db.Integer, db.ForeignKey('siswa.id'), nullable=False)
    ekskul_id = db.Column(db.Integer, db.ForeignKey('jenis_ekskul.id'), nullable=False)
    semester_id = db.Column(db.Integer, db.ForeignKey('semester.id'), nullable=False)
    
    predikat = db.Column(db.String(2)) # A/B/C/D
    deskripsi = db.Column(db.Text)

    siswa = db.relationship('Siswa', back_populates='ekskul')
    ekskul = db.relationship('JenisEkskul', back_populates='nilai_ekskul')
    semester = db.relationship('Semester', back_populates='ekskul')
    
    def __repr__(self):
        return f"<NilaiEkskul Siswa ID={self.siswa_id} Ekskul ID={self.ekskul_id}>"
