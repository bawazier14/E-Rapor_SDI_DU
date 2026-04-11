from flask import Blueprint

mapel_bp = Blueprint('mapel', __name__, template_folder='templates')

from app.modules.mapel import routes
