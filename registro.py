from flask import Blueprint, request, jsonify
from database import db

Registro_bp = Blueprint('registro', __name__)
coleccion = db['registros']  # Colección en MongoDB

@Registro_bp.route('/api/registro', methods=['POST'])
def registrar_usuario():
    try:
        datos = request.json
        print("📥 Datos recibidos en Registro:", datos)
        
        # Guarda en la base de datos
        coleccion.insert_one(datos.copy())
        return jsonify({"message": "Registro completado exitosamente"}), 201
    except Exception as e:
        print("Error en Registro:", e)
        return jsonify({"message": "Error al procesar registro", "error": str(e)}), 500