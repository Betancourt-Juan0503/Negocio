from flask import Blueprint, request, jsonify
from database import db

informacion_admin_bp = Blueprint('informacion_admin', __name__)
coleccion = db['informacion_admin'] 

@informacion_admin_bp.route('/api/informacion_admin', methods=['POST'])
def registrar_admin():
    try:
        datos = request.json
        print(" Datos recibidos en Información Admin:", datos)
        
 
        coleccion.insert_one(datos.copy())
        return jsonify({"message": "Información administrativa guardada exitosamente"}), 201
    except Exception as e:
        print("Error en Información Admin:", e)
        return jsonify({"message": "Error al guardar información admin", "error": str(e)}), 500
