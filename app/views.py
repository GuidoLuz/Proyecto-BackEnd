from flask import jsonify, request
from app.models import Paquete


def index():
    response = {"message":"Hello World API Cac-movies"}
    return jsonify(response)

# funcion que busca todo el listado de los paquetes
def get_all_paquetes():
    paquetes= Paquete.get_all()
    list_paquetes = [paquete.serialize() for paquete in paquetes]
    return jsonify(list_paquetes)

# funcion que busca un paquete
def get_paquete(paquete_id):
    paquete = Paquete.get_by_id(paquete_id)
    if not paquete:
        return jsonify({'message': 'paquete no encontrada'}), 404
    return jsonify(paquete.serialize())

# funcion que crea un paquete
def create_paquete():
    data = request.json
    new_paquete = Paquete(None,data["ciudad"],data["dias"],data["precio"],data["banner"])
    new_paquete.save()
    return jsonify({"message":"Paquete creada con exito"}),201

# funcion que actualiza 
def update_paquete(paquete_id):
    paquete = Paquete.get_by_id(paquete_id)
    if not paquete:
        return jsonify({'message': 'Paquete no encontrada'}), 404
    data = request.json
    paquete.ciudad = data['ciudad']
    paquete.dias = data['dias']
    paquete.precio = data['precio']
    paquete.banner = data['banner']
    paquete.save()
    return jsonify({'message': 'Paquete actualizada con éxito'})

# funcion que elimina un paquete
def delete_paquete(paquete_id):
    paquete = Paquete.get_by_id(paquete_id)
    if not paquete:
        return jsonify({'message': 'Paquete no encontrada'}), 404
    paquete.delete()
    return jsonify({'message': 'Paquete eliminada con éxito'})