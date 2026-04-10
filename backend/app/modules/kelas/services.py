from app.extensions import db
from app.models.kelas import Kelas

class KelasService:
    @staticmethod
    def get_all_kelas():
        return Kelas.query.order_by(Kelas.tingkat).all()

    @staticmethod
    def get_kelas_by_id(kelas_id):
        return Kelas.query.get_or_404(kelas_id)

    @staticmethod
    def create_kelas(data):
        # Check if tingkat already exists
        existing = Kelas.query.filter_by(tingkat=data['tingkat']).first()
        if existing:
            raise ValueError(f"Tingkat {data['tingkat']} sudah terdaftar.")
            
        kelas = Kelas(
            tingkat=data['tingkat'],
            nama_tingkat=data['nama_tingkat'],
            fase=data['fase']
        )
        db.session.add(kelas)
        db.session.commit()
        return kelas

    @staticmethod
    def update_kelas(kelas_id, data):
        kelas = Kelas.query.get_or_404(kelas_id)
        
        # Check if new tingkat conflicts with other records
        if kelas.tingkat != data['tingkat']:
            existing = Kelas.query.filter_by(tingkat=data['tingkat']).first()
            if existing:
                raise ValueError(f"Tingkat {data['tingkat']} sudah terdaftar.")
        
        kelas.tingkat = data['tingkat']
        kelas.nama_tingkat = data['nama_tingkat']
        kelas.fase = data['fase']
        
        db.session.commit()
        return kelas

    @staticmethod
    def delete_kelas(kelas_id):
        kelas = Kelas.query.get_or_404(kelas_id)
        # Check if there are rombels linked to this class
        if kelas.rombels:
            raise ValueError("Tidak dapat menghapus tingkat kelas yang masih memiliki rombel.")
            
        db.session.delete(kelas)
        db.session.commit()
        return True
