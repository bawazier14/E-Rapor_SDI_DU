from flask import Blueprint

sekolah_bp = Blueprint(
    'sekolah',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from app.modules.sekolah import routes
