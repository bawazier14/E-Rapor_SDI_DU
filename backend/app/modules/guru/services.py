from app.extensions import db
from app.models.guru import Guru
from app.models.user import User
from app.models.role import Role
from werkzeug.security import generate_password_hash

class GuruService:
    @staticmethod
    def get_all_guru():
        return Guru.query.all()

    @staticmethod
    def get_guru_by_id(guru_id):
        return db.session.get(Guru, guru_id)

    @staticmethod
    def create_guru(data, create_user=False):
        guru = Guru(
            nip=data.get('nip'),
            nuptk=data.get('nuptk'),
            nama_lengkap=data.get('nama_lengkap'),
            jenis_kelamin=data.get('jenis_kelamin'),
            tempat_lahir=data.get('tempat_lahir'),
            tanggal_lahir=data.get('tanggal_lahir'),
            agama=data.get('agama'),
            alamat=data.get('alamat'),
            no_hp=data.get('no_hp'),
            status_aktif=data.get('status_aktif', True)
        )
        db.session.add(guru)
        db.session.flush() # To get guru.id

        if create_user:
            GuruService._create_user_account(guru)

        db.session.commit()
        return guru

    @staticmethod
    def update_guru(guru, data, sync_user=False):
        guru.nip = data.get('nip')
        guru.nuptk = data.get('nuptk')
        guru.nama_lengkap = data.get('nama_lengkap')
        guru.jenis_kelamin = data.get('jenis_kelamin')
        guru.tempat_lahir = data.get('tempat_lahir')
        guru.tanggal_lahir = data.get('tanggal_lahir')
        guru.agama = data.get('agama')
        guru.alamat = data.get('alamat')
        guru.no_hp = data.get('no_hp')
        guru.status_aktif = data.get('status_aktif', guru.status_aktif)

        if sync_user and not guru.user:
            GuruService._create_user_account(guru)
        elif not sync_user and guru.user:
            # Optionally handle user account removal if needed
            pass

        db.session.commit()
        return guru

    @staticmethod
    def toggle_guru_status(guru):
        guru.status_aktif = not guru.status_aktif
        if guru.user:
            guru.user.is_active = guru.status_aktif
        db.session.commit()
        return guru

    @staticmethod
    def _create_user_account(guru):
        # Generate username from nama_lengkap (lowercase, no spaces)
        username = "".join(guru.nama_lengkap.split()).lower()
        # Check if username exists, append NIP or random if it does
        base_username = username
        counter = 1
        while User.query.filter_by(username=username).first():
            username = f"{base_username}{counter}"
            counter += 1

        guru_role = Role.query.filter_by(name='Guru').first()
        if not guru_role:
            guru_role = Role(name='Guru', description='Wali Kelas / Guru Pengajar')
            db.session.add(guru_role)
            db.session.flush()

        user = User(
            username=username,
            password_hash=generate_password_hash('guru123'), # Default password
            is_active=True
        )
        user.role = guru_role
        db.session.add(user)
        db.session.flush()
        
        guru.user_id = user.id
