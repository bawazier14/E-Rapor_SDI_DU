from app.extensions import db
from app.models.base import BaseModel

class Mapel(BaseModel):
    __tablename__ = 'mapel'

    kode = db.Column(db.String(20), unique=True, nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    kelompok = db.Column(db.String(10)) # A, B, Mulok
    urutan = db.Column(db.Integer, default=0) # For displaying sorting order
    status_aktif = db.Column(db.Boolean, default=True)

    # Mengajar instances
    mengajar = db.relationship('Mengajar', back_populates='mapel')

    def __repr__(self):
        return f"<Mapel {self.nama}>"
