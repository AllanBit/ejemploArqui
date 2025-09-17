from flask import Flask, jsonify, request

# Datos de prueba (lista de diccionarios), se puede obtener de una base de datos de SQLite con JSON
ests = [
    {"nombre": "Juan", 
     "apellido": 
     "Perez", 
     "edad": 20},

    {"nombre": 
     "Diego", 
     "apellido": 
     "Hernandez", 
     "edad": 70}
]



#Funciones para servir los datos desde una lista de diccionarios
def mostrarEstudiante(id):
    try:
        i = int(id)
        return ests[i]
    except:
        return None

def agregar(est):
    try:
        ests.append(est)
        return True
    except:
        return False

def eliminar(id):
    try:
        i = int(id)
        ests.pop(i)
        return True
    except:
        return False
    
def modificar(id, data):
    try:
        i = int(id)
        ests[i] = data
        return True
    except:
        return False



# Inicio del servidor
app = Flask(__name__)

# -----------------------Endpoints---------------------

#Endpoint de prueba :D
@app.route("/yo", methods=['GET'])
def saludar():
    return "Me gustan los jokeis :D", 200


#Endpoint base
@app.route("/")
def root():
    return "Servidor funcionando", 200

#Endpoint para obtener estudiantes
@app.route("/estudiantes", methods=['GET'])
def getEstudiantes():
    return jsonify(ests), 200

#Endpoint para obtener solo un estudiante con un decorador
@app.route("/estudiantes/<id>", methods=['GET'])
def getEstudiante(id):
    est = mostrarEstudiante(id)
    if est:
        return jsonify(est), 200
    else:
        return jsonify({"mensaje": "Estudiante no encontrado"}), 404

#Enpoint para crear un nuevo estudiante
@app.route("/estudiantes", methods=['POST'])
def postEstudiantes():
    data = request.get_json()
    
    if agregar(data):
        return jsonify(data), 201
    else:
        return jsonify({"mensaje": "Error al crear estudiante"}), 500

#Endpoint para eliminar un estudiante
@app.route("/estudiantes/<id>", methods=['DELETE'])
def deleteEstudiantes(id):
    if eliminar(id):
        return jsonify({"mensaje": "Eliminado exitosamente"}), 200
    else:
        return jsonify({"mensaje": "Error eliminando, índice no válido"}), 404


@app.route("/estudiantes/<id>", methods=['PUT'])
def updateEstudiantes(id):
    data = request.get_json()
    
    if modificar(id, data):
        return jsonify(data), 200
    else:
        return jsonify({"mensaje": "Error al modificar estudiante"}), 500



if __name__ == "__main__":
    app.run(debug=True)
