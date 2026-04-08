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
        db.session.commit()
        return user

    @staticmethod
    def update_user(user, data):
        user.username = data['username']
        user.role_id = data['role_id']
        user.is_active = data['is_active']
        db.session.commit()
        return user

    @staticmethod
    def toggle_user_status(user):
        user.is_active = not user.is_active
        db.session.commit()
        return user

    @staticmethod
    def reset_password(user, new_password):
        user.set_password(new_password)
        db.session.commit()
        return user
