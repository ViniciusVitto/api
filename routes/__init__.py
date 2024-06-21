from flask import Blueprint

usuario_bp = Blueprint('usuario_bp', __name__)
conta_bp = Blueprint('conta_bp', __name__)

from .usuario_routes import *
from .conta_routes import *
