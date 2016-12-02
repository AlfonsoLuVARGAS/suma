"""prueba de programación UNACIONAL."""
from flask import Flask, render_template
from flask_wtf.csrf import CsrfProtect

import forms

__author__ = 'Alfonso Luis Vargas Amaya'

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
csrf = CsrfProtect()


@app.route('/')
def index():
    """Envia formulario por metodo get"""
    suma_form = forms.sumaForm()
    return render_template('index.html', form=suma_form)


if __name__ == '__main__':
    if __name__ == '__main__':
        csrf.init_app(app)
        app.run(debug=True, port=8000)
