from flask import Flask
from app.database import init_app
from app.views import *
from flask_cors import CORS

app = Flask(__name__)
init_app(app)

# Permitir solicitudes desde cualquier origen
CORS(app)

# Rutas de la API-REST

app.route("/", methods=["GET"])(index)
app.route("/api/paquetes/",methods=["GET"])(get_all_paquetes)
app.route("/api/paquetes/",methods=["POST"])(create_paquete)
app.route('/api/paquetes/<int:paquete_id>', methods=['GET'])(get_paquete)
app.route('/api/paquetes/<int:paquete_id>', methods=['PUT'])(update_paquete)
app.route('/api/paquetes/<int:paquete_id>', methods=['DELETE'])(delete_paquete)

if __name__== "__main__":
    app.run(debug=True)