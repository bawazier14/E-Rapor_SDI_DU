from app.extensions import db
from app.models.base import BaseModel

class Kelas(BaseModel):
    __tablename__ = 'kelas'

    tingkat = db.Column(db.Integer, nullable=False, unique=True) # 1, 2, 3, 4, 5, 6
    nama_tingkat = db.Column(db.String(20), nullable=False) # Kelas 1, Kelas 2
    fase = db.Column(db.String(10)) # A, B, C (Kurikulum Merdeka)

    rombels = db.relationship('Rombel', back_populates='kelas')

    def __repr__(self):
        return f"<Kelas {self.nama_tingkat}>"
