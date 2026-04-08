from app.extensions import db
from app.models.base import BaseModel

class Mengajar(BaseModel):
    __tablename__ = 'mengajar'

    guru_id = db.Column(db.Integer, db.ForeignKey('guru.id'), nullable=False)
    mapel_id = db.Column(db.Integer, db.ForeignKey('mapel.id'), nullable=False)
    rombel_id = db.Column(db.Integer, db.ForeignKey('rombel.id'), nullable=False)
    
    guru = db.relationship('Guru', back_populates='mengajar')
    mapel = db.relationship('Mapel', back_populates='mengajar')
    rombel = db.relationship('Rombel', back_populates='mengajar')
    
    # Nilai dari mapel ini diajar oleh guru ini
    nilai = db.relationship('Nilai', back_populates='mengajar')

    def __repr__(self):
        return f"<Mengajar Guru ID={self.guru_id} Mapel ID={self.mapel_id}>"
