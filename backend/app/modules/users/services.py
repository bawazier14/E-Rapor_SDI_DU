from app.models.user import User
from app.models.role import Role
from app.extensions import db

class UserService:
    @staticmethod
    def get_all_users():
        return User.query.options(db.joinedload(User.role)).all()

    @staticmethod
    def get_user_by_id(user_id):
        return db.session.get(User, user_id)

    @staticmethod
    def get_all_roles():
        return Role.query.all()

    @staticmethod
    def create_user(data):
        user = User(
            username=data['username'],
            role_id=data['role_id'],
            is_active=data['is_active']
        )
        user.set_password(data['password'])
        db.session.add(user)
        db.session.flush() # Get user.id

        # Auto-create Guru profile if role is Guru (ID: 2)
        if user.role_id == 2:
            from app.modules.guru.services import GuruService
            GuruService.create_skeleton_guru(user)

        db.session.commit()
        return user

    @staticmethod
    def update_user(user, data):
        old_role_id = user.role_id
        user.username = data['username']
        user.role_id = data['role_id']
        user.is_active = data['is_active']
        
        # If changed TO Guru role and no profile exists
        if user.role_id == 2 and old_role_id != 2:
            if not user.guru:
                from app.modules.guru.services import GuruService
                GuruService.create_skeleton_guru(user)
        
        # Sync status to Guru profile if exists
        if user.guru:
            user.guru.status_aktif = user.is_active

        db.session.commit()
        return user

    @staticmethod
    def toggle_user_status(user):
        user.is_active = not user.is_active
        # Sync status to Guru profile if exists
        if user.guru:
            user.guru.status_aktif = user.is_active
        db.session.commit()
        return user

    @staticmethod
    def reset_password(user, new_password):
        user.set_password(new_password)
        db.session.commit()
        return user
