from app.extensions import db
from app.models.base import BaseModel

class Rapor(BaseModel):
    __tablename__ = 'rapor'
    
    siswa_id = db.Column(db.Integer, db.ForeignKey('siswa.id'), nullable=False)
    semester_id = db.Column(db.Integer, db.ForeignKey('semester.id'), nullable=False)
    
    # Metadata for archival
    is_final = db.Column(db.Boolean, default=False)
    tanggal_terbit = db.Column(db.Date)
    pdf_path = db.Column(db.String(255)) # Path relative to UPLOAD_FOLDER for the generated PDF
    
    siswa = db.relationship('Siswa', back_populates='rapor')
    semester = db.relationship('Semester', back_populates='rapor')

    def __repr__(self):
        return f"<Rapor Siswa ID={self.siswa_id} Semester ID={self.semester_id}>"
