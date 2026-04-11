from app.extensions import db
from app.models.mapel import Mapel

class MapelService:
    @staticmethod
    def get_all_mapel():
        return Mapel.query.order_by(Mapel.urutan.asc(), Mapel.kelompok.asc()).all()

    @staticmethod
    def get_mapel_by_id(mapel_id):
        return Mapel.query.get_or_404(mapel_id)

    @staticmethod
    def create_mapel(data):
        # Cek kode duplikat
        existing = Mapel.query.filter_by(kode=data['kode']).first()
        if existing:
            raise ValueError(f"Mata Pelajaran dengan kode {data['kode']} sudah ada.")
            
        mapel = Mapel(
            kode=data['kode'],
            nama=data['nama'],
            kelompok=data['kelompok'],
            urutan=data['urutan'],
            status_aktif=data['status_aktif']
        )
        db.session.add(mapel)
        db.session.commit()
        return mapel

    @staticmethod
    def update_mapel(mapel_id, data):
        mapel = MapelService.get_mapel_by_id(mapel_id)
        
        # Validasi kode duplikat jika diganti
        if mapel.kode != data['kode']:
            existing = Mapel.query.filter_by(kode=data['kode']).first()
            if existing:
                raise ValueError(f"Mata Pelajaran dengan kode {data['kode']} sudah ada.")
        
        mapel.kode = data['kode']
        mapel.nama = data['nama']
        mapel.kelompok = data['kelompok']
        mapel.urutan = data['urutan']
        mapel.status_aktif = data['status_aktif']
        
        db.session.commit()
        return mapel

    @staticmethod
    def delete_mapel(mapel_id):
        mapel = MapelService.get_mapel_by_id(mapel_id)
        if mapel.mengajar:
            raise ValueError("Tidak dapat menghapus mapel yang sudah memiliki penugasan mengajar (relasi).")
        
        db.session.delete(mapel)
        db.session.commit()
        return True
