from flask import Blueprint

kelas_bp = Blueprint('kelas', __name__, template_folder='templates')

from app.modules.kelas import routes
