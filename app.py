from flask import Flask
from flask_cors import CORS 


from routes.index import index_bp
from routes.control_ingresos import Control_ingresos_bp
from routes.doctores import Doctores_bp
from routes.facturas import Facturas_bp
from routes.historial_clinico import Historial_clinico_bp
from routes.informacion_admin import informacion_admin_bp
from routes.inventario import Inventario_bp
from routes.registro import Registro_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(index_bp)
app.register_blueprint(Control_ingresos_bp)
app.register_blueprint(Doctores_bp)
app.register_blueprint(Facturas_bp)
app.register_blueprint(Historial_clinico_bp)
app.register_blueprint(informacion_admin_bp)
app.register_blueprint(Inventario_bp)
app.register_blueprint(Registro_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)