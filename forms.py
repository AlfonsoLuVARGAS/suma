"""forms.py file."""
from wtforms import Form, StringField, validators


class sumaForm(Form):
    first_number = StringField('Text number one', [
        validators.Required(message='Número es requerido!')
    ])
    second_number = StringField('Text number two', [
        validators.Required(message='Número es requerido!')
    ])
