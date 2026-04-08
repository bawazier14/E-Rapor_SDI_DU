import os
from werkzeug.utils import secure_filename
from flask import current_app
from app.extensions import db
from app.models.sekolah import Sekolah

class SekolahService:
    @staticmethod
    def get_sekolah():
        sekolah = Sekolah.query.first()
        if not sekolah:
            # Create a default record if none exists
            sekolah = Sekolah(nama="E-Rapor SD Default", npsn="00000000")
            db.session.add(sekolah)
            db.session.commit()
        return sekolah

    @staticmethod
    def update_sekolah(sekolah, data, logo_file=None):
        sekolah.nama = data.get('nama')
        sekolah.npsn = data.get('npsn')
        sekolah.alamat = data.get('alamat')
        sekolah.kode_pos = data.get('kode_pos')
        sekolah.desa_kelurahan = data.get('desa_kelurahan')
        sekolah.kecamatan = data.get('kecamatan')
        sekolah.kabupaten_kota = data.get('kabupaten_kota')
        sekolah.provinsi = data.get('provinsi')
        sekolah.website = data.get('website')
        sekolah.email = data.get('email')
        sekolah.kepala_sekolah = data.get('kepala_sekolah')
        sekolah.nip_kepala_sekolah = data.get('nip_kepala_sekolah')

        if logo_file:
            filename = secure_filename(f"logo_{sekolah.npsn}_{logo_file.filename}")
            upload_dir = os.path.join(current_app.static_folder, 'uploads', 'sekolah')
            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)
            
            logo_path = os.path.join(upload_dir, filename)
            logo_file.save(logo_path)
            sekolah.logo_path = f"uploads/sekolah/{filename}"

        db.session.commit()
        return sekolah
