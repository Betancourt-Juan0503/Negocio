from flask import Blueprint, request, jsonify
from database import db
from bson import ObjectId

Facturas_bp = Blueprint('facturas', __name__)
coleccion = db['facturas']

@Facturas_bp.route('/api/facturas', methods=['GET', 'POST'])
def registrar_factura():
    try:
        if request.method == 'POST':
            datos = request.json
            print("📥 Datos recibidos en Facturas:", datos)
            coleccion.insert_one(datos.copy())
            return jsonify({"message": "Factura guardada exitosamente"}), 201
            
        if request.method == 'GET':
            facturas = list(coleccion.find())
            for f in facturas:
                f['_id'] = str(f['_id'])
            return jsonify(facturas), 200
            
    except Exception as e:
        print("Error en Facturas:", e)
        return jsonify({"message": "Error en el servidor", "error": str(e)}), 500

@Facturas_bp.route('/api/facturas/<id>', methods=['DELETE'])
def eliminar_factura(id):
    try:
        resultado = coleccion.delete_one({"_id": ObjectId(id)})
        if resultado.deleted_count > 0:
            return jsonify({"message": "Factura eliminada exitosamente"}), 200
        else:
            return jsonify({"message": "No se encontró la factura"}), 404
    except Exception as e:
        try:
            resultado = coleccion.delete_one({"id_factura": id})
            if resultado.deleted_count > 0:
                return jsonify({"message": "Factura eliminada exitosamente"}), 200
            return jsonify({"message": "No se encontró la factura"}), 404
        except:
            return jsonify({"message": "Error al eliminar factura", "error": str(e)}), 500