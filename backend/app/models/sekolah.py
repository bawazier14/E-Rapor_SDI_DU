from app.extensions import db
from app.models.base import BaseModel

class Sekolah(BaseModel):
    __tablename__ = 'sekolah'

    nama = db.Column(db.String(100), nullable=False)
    npsn = db.Column(db.String(20), unique=True, nullable=False)
    alamat = db.Column(db.Text)
    kode_pos = db.Column(db.String(10))
    desa_kelurahan = db.Column(db.String(50))
    kecamatan = db.Column(db.String(50))
    kabupaten_kota = db.Column(db.String(50))
    provinsi = db.Column(db.String(50))
    website = db.Column(db.String(100))
    email = db.Column(db.String(100))
    kepala_sekolah = db.Column(db.String(100))
    nip_kepala_sekolah = db.Column(db.String(30))
    logo_path = db.Column(db.String(255))

    def __repr__(self):
        return f"<Sekolah {self.nama}>"
