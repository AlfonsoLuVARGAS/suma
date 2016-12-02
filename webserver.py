"""prueba de programación UNACIONAL."""
from flask import Flask, render_template, request, flash
from flask_wtf.csrf import CsrfProtect
from helper import english_numbers

import forms

__author__ = 'Alfonso Luis Vargas Amaya'

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
csrf = CsrfProtect()


@app.route('/', methods=['GET', 'POST'])
def index():
    """Envia formulario por metodo get valida en post.
    Esta función devuelve la suma de dos numeros en inglés."""
    suma_form = forms.sumaForm(request.form)
    if request.method == 'POST' and suma_form.validate():
        numbers = english_numbers()
        fi = suma_form.first_number.data
        se = suma_form.second_number.data
        pos = 0
        for num in numbers:
            num = num.lower()
            if num == fi:
                pos_fi = pos
                print(pos)
            if num == se:
                pos_se = pos
                print(pos)
            pos = pos + 1
        suma = pos_fi + pos_se
        success_message = 'The sum is {}'.format(numbers[suma])
        flash(success_message)
        return render_template('index.html', form=suma_form)
    else:
        print("Error en formulario")
    return render_template('index.html', form=suma_form)


if __name__ == '__main__':
    if __name__ == '__main__':
        csrf.init_app(app)
        app.run(port=8000)
