from flask import Blueprint

guru_bp = Blueprint(
    'guru',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from app.modules.guru import routes
