from flask import Blueprint, request, jsonify
from database import db

Historial_clinico_bp = Blueprint('historial_clinico', __name__)
coleccion = db['historial_clinico'] 

@Historial_clinico_bp.route('/api/historial_clinico', methods=['POST'])
def registrar_historial():
    try:
        datos = request.json
        print(" Datos recibidos en Historial Clínico:", datos)
        
      
        coleccion.insert_one(datos.copy())
        return jsonify({"message": "Historial clínico guardado exitosamente"}), 201
    except Exception as e:
        print("Error en Historial Clínico:", e)
        return jsonify({"message": "Error al guardar historial", "error": str(e)}), 500
