from functools import wraps
from flask import abort
from flask_login import current_user

def roles_required(*roles):
    """
    Custom decorator to protect routes based on User Role.
    Usage: @roles_required('Admin', 'Guru')
    Must be placed after @login_required
    """
    def decorator(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
                return abort(401)
                
            if not current_user.role or current_user.role.name not in roles:
                # User does not have the required role
                return abort(403)
                
            return func(*args, **kwargs)
        return decorated_view
    return decorator
