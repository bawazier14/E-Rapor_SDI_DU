from app.extensions import db
from app.models.base import BaseModel

class TahunAjaran(BaseModel):
    __tablename__ = 'tahun_ajaran'

    nama = db.Column(db.String(20), unique=True, nullable=False) # e.g. 2023/2024
    status_aktif = db.Column(db.Boolean, default=False)
    
    semesters = db.relationship('Semester', back_populates='tahun_ajaran')
    rombels = db.relationship('Rombel', back_populates='tahun_ajaran')

    def __repr__(self):
        return f"<TahunAjaran {self.nama}>"
