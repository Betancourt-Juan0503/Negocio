from flask import Blueprint, request, jsonify
from database import db 

Control_ingresos_bp = Blueprint('control_ingresos', __name__)
coleccion = db['control_ingresos'] 

@Control_ingresos_bp.route('/api/control_ingresos', methods=['POST'])
def registrar_ingreso():
    try:
        datos = request.json
        print(" Datos recibidos en Control de Ingresos:", datos)
        
    
        coleccion.insert_one(datos.copy())
        return jsonify({"message": "Ingreso guardado exitosamente"}), 201
    except Exception as e:
        print("Error en Control de Ingresos:", e)
        return jsonify({"message": "Error al guardar ingreso", "error": str(e)}), 500
