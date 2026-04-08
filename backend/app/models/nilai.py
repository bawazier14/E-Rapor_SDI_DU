from app.extensions import db
from app.models.base import BaseModel

class Nilai(BaseModel):
    __tablename__ = 'nilai'

    siswa_id = db.Column(db.Integer, db.ForeignKey('siswa.id'), nullable=False)
    mengajar_id = db.Column(db.Integer, db.ForeignKey('mengajar.id'), nullable=False)
    semester_id = db.Column(db.Integer, db.ForeignKey('semester.id'), nullable=False)
    
    # Nilai fields
    nilai_formatif = db.Column(db.Float)
    nilai_sumatif = db.Column(db.Float)
    nilai_pts = db.Column(db.Float)
    nilai_pas = db.Column(db.Float)
    nilai_akhir = db.Column(db.Float)
    predikat = db.Column(db.String(2)) # A, B, C, D
    deskripsi = db.Column(db.Text)
    
    status_final = db.Column(db.Boolean, default=False) # If true, locked.

    siswa = db.relationship('Siswa', back_populates='nilai')
    mengajar = db.relationship('Mengajar', back_populates='nilai')
    semester = db.relationship('Semester', back_populates='nilai')

    def __repr__(self):
        return f"<Nilai Siswa ID={self.siswa_id} Mengajar ID={self.mengajar_id}>"
