from app.models.user import User

class AuthService:
    @staticmethod
    def authenticate_user(username, password):
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            # Also ensure user is active before allowing login
            if user.is_active:
                return user
        return None
