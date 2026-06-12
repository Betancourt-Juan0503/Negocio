from flask import Blueprint, jsonify, request
from bson import ObjectId
from database import db

Inventario_bp = Blueprint('inventario_bp', __name__)

@Inventario_bp.route('/api/inventario', methods=['GET', 'POST'])
def manejar_inventario():
    if request.method == 'POST':
        try:
            datos = request.get_json()
            
            nuevo_med = {
                "id_med": datos.get("id_med"),
                "medicamento": datos.get("medicamento"),
                "presentacion": datos.get("presentacion"),
                "stock_inicial": datos.get("stock_inicial"),
                "cantidad_usada": datos.get("cantidad_usada"),
                "precio_unitario": datos.get("precio_unitario"),
                "caducidad": datos.get("caducidad")
            }
            
            resultado = db.inventario.insert_one(nuevo_med)
            nuevo_med["_id"] = str(resultado.inserted_id)
            
            return jsonify({"data": nuevo_med}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    try:
        registros = list(db.inventario.find())
        print(f"--- DETECTIVE FLASK: Se encontraron {len(registros)} registros en la colección 'inventario' ---")
        
        for reg in registros:
            reg['_id'] = str(reg['_id'])
            
        return jsonify(registros), 200
    except Exception as e:
        print(f"--- DETECTIVE FLASK ERROR: {str(e)} ---")
        return jsonify({"error": str(e)}), 500

@Inventario_bp.route('/api/inventario/<id>', methods=['DELETE', 'PUT', 'OPTIONS'])
def eliminar_o_actualizar_inventario(id):
    if request.method == 'OPTIONS':
        return jsonify({"status": "ok"}), 200
        
    if request.method == 'PUT':
        try:
            datos = request.get_json()
            resultado = db.inventario.update_one(
                {"_id": ObjectId(id)},
                {"$set": {
                    "id_med": datos.get("id_med"),
                    "medicamento": datos.get("medicamento"),
                    "presentacion": datos.get("presentacion"),
                    "stock_inicial": datos.get("stock_inicial"),
                    "cantidad_usada": datos.get("cantidad_usada"),
                    "precio_unitario": datos.get("precio_unitario"),
                    "caducidad": datos.get("caducidad")
                }}
            )
            if resultado.matched_count > 0:
                return jsonify({"mensaje": "Actualizado con éxito"}), 200
            return jsonify({"error": "No se encontró el registro"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    if request.method == 'DELETE':
        try:
            resultado = db.inventario.delete_one({"_id": ObjectId(id)})
            if resultado.deleted_count > 0:
                return jsonify({"mensaje": "Eliminado con éxito"}), 200
            return jsonify({"error": "No se encontró el registro"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500