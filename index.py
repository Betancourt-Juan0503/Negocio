from flask import Blueprint

index_bp = Blueprint('index', __name__)

@index_bp.route('/', methods=['GET'])
def inicio():
    return "Servidor local de Medicare activo y funcionando."