from app.extensions import db
from app.models.base import BaseModel

class Absensi(BaseModel):
    __tablename__ = 'absensi'

    siswa_id = db.Column(db.Integer, db.ForeignKey('siswa.id'), nullable=False)
    rombel_id = db.Column(db.Integer, db.ForeignKey('rombel.id'), nullable=False)
    semester_id = db.Column(db.Integer, db.ForeignKey('semester.id'), nullable=False)
    
    sakit = db.Column(db.Integer, default=0)
    izin = db.Column(db.Integer, default=0)
    alfa = db.Column(db.Integer, default=0)

    siswa = db.relationship('Siswa', back_populates='absensi')
    rombel = db.relationship('Rombel', back_populates='absensi')
    semester = db.relationship('Semester', back_populates='absensi')

    def __repr__(self):
        return f"<Absensi Siswa ID={self.siswa_id}>"
