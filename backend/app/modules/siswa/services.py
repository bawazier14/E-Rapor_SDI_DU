from app.extensions import db
from app.models.siswa import Siswa
from app.models.user import User

class SiswaService:
    @staticmethod
    def get_all_siswa():
        return Siswa.query.all()

    @staticmethod
    def get_siswa_by_id(siswa_id):
        return db.session.get(Siswa, siswa_id)

    @staticmethod
    def create_siswa(data):
        siswa = Siswa(
            nisn=data.get('nisn'),
            nis=data.get('nis'),
            nama_lengkap=data.get('nama_lengkap'),
            jenis_kelamin=data.get('jenis_kelamin'),
            tempat_lahir=data.get('tempat_lahir'),
            tanggal_lahir=data.get('tanggal_lahir'),
            agama=data.get('agama'),
            alamat=data.get('alamat'),
            nama_ayah=data.get('nama_ayah'),
            nama_ibu=data.get('nama_ibu'),
            pekerjaan_ayah=data.get('pekerjaan_ayah'),
            pekerjaan_ibu=data.get('pekerjaan_ibu'),
            alamat_orang_tua=data.get('alamat_orang_tua'),
            no_hp_orang_tua=data.get('no_hp_orang_tua'),
            status_aktif=data.get('status_aktif', 'aktif')
        )
        db.session.add(siswa)
        db.session.commit()
        return siswa

    @staticmethod
    def update_siswa(siswa, data):
        siswa.nisn = data.get('nisn')
        siswa.nis = data.get('nis')
        siswa.nama_lengkap = data.get('nama_lengkap')
        siswa.jenis_kelamin = data.get('jenis_kelamin')
        siswa.tempat_lahir = data.get('tempat_lahir')
        siswa.tanggal_lahir = data.get('tanggal_lahir')
        siswa.agama = data.get('agama')
        siswa.alamat = data.get('alamat')
        siswa.nama_ayah = data.get('nama_ayah')
        siswa.nama_ibu = data.get('nama_ibu')
        siswa.pekerjaan_ayah = data.get('pekerjaan_ayah')
        siswa.pekerjaan_ibu = data.get('pekerjaan_ibu')
        siswa.alamat_orang_tua = data.get('alamat_orang_tua')
        siswa.no_hp_orang_tua = data.get('no_hp_orang_tua')
        siswa.status_aktif = data.get('status_aktif', siswa.status_aktif)
        
        db.session.commit()
        return siswa

    @staticmethod
    def delete_siswa(siswa):
        db.session.delete(siswa)
        db.session.commit()
