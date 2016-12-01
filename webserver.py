"""prueba de programación UNACIONAL."""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """Servicio flask en ejecución."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
