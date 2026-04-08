from flask import Blueprint

auth_bp = Blueprint(
    'auth', 
    __name__, 
    template_folder='templates',
    static_folder='static'
)

# Import routes down here to avoid circular imports
from app.modules.auth import routes
