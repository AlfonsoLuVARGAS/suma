# Importa libreria
from flask import Flask, request


# Instancia la variable acipet con la constanten "__name__"
app = Flask(__name__)

# WRAP: se llama el metodo route con la url raiz y se retorna la funcion 'def index'
@app.route('/')
def index():
    return 'Servicio flask corriendo...'

# se llama el metodo run que ejecuta el servidor en el puerto 5000
if __name__ == '__main__':
    app.run(debug=True)
