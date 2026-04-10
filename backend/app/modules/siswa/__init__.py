from flask import Blueprint

siswa_bp = Blueprint('siswa', __name__, template_folder='templates')

from app.modules.siswa import routes
