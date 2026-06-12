from flask import Blueprint, request, jsonify
from bson import ObjectId
from database import db

Doctores_bp = Blueprint('doctores', __name__)
coleccion = db['doctores']

@Doctores_bp.route('/api/doctores', methods=['POST', 'GET', 'OPTIONS'])
def manejar_doctores():
    if request.method == 'OPTIONS':
        return jsonify({"status": "ok"}), 200

    if request.method == 'POST':
        try:
            datos = request.json
            print(" Datos recibidos en Doctores:", datos)
            coleccion.insert_one(datos.copy())
            return jsonify({"message": "Doctor guardado exitosamente"}), 201
        except Exception as e:
            return jsonify({"message": "Error al guardar doctor", "error": str(e)}), 500

    if request.method == 'GET':
        try:
            registros = list(coleccion.find())
            print("=== PYTHON ENCONTRÓ ESTOS DOCTORES ===", registros)
            for reg in registros:
                reg['_id'] = str(reg['_id'])
            return jsonify(registros), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@Doctores_bp.route('/api/doctores/<id>', methods=['DELETE', 'PUT', 'OPTIONS'])
def eliminar_doctor(id):
    if request.method == 'OPTIONS':
        return jsonify({"status": "ok"}), 200
        
    if request.method == 'PUT':
        try:
            datos = request.json
            resultado = coleccion.update_one(
                {"_id": ObjectId(id)},
                {"$set": {
                    "id_doc": datos.get("id_doc"),
                    "nombre": datos.get("nombre"),
                    "especialidad": datos.get("especialidad"),
                    "telefono": datos.get("telefono"),
                    "correo": datos.get("correo"),
                    "horario": datos.get("horario")
                }}
            )
            if resultado.matched_count > 0:
                return jsonify({"mensaje": "Doctor actualizado con éxito"}), 200
            return jsonify({"error": "No se encontró el registro"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    if request.method == 'DELETE':
        try:
            resultado = coleccion.delete_one({"_id": ObjectId(id)})
            if resultado.deleted_count > 0:
                return jsonify({"mensaje": "Eliminado con éxito"}), 200
            return jsonify({"error": "No se encontró el registro"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500