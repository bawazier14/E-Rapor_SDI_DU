from app.extensions import db
from app.models.base import BaseModel

class CatatanWaliKelas(BaseModel):
    __tablename__ = 'catatan_wali_kelas'
    
    siswa_id = db.Column(db.Integer, db.ForeignKey('siswa.id'), nullable=False)
    semester_id = db.Column(db.Integer, db.ForeignKey('semester.id'), nullable=False)
    
    catatan = db.Column(db.Text)
    
    siswa = db.relationship('Siswa', back_populates='catatan')
    semester = db.relationship('Semester', back_populates='catatan')

    def __repr__(self):
        return f"<CatatanWaliKelas Siswa ID={self.siswa_id}>"
