"""forms.py file."""
from wtforms import Form, StringField, validators, HiddenField
from helper import english_numbers


def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo no está vacío.')


def field_text(form, field):
    campo = field.data
    if campo.isdigit():
        raise validators.ValidationError('El campo no puede ser numérico.')


def field_exist(form, field):
    number = field.data
    number = number.lower()
    numbers = english_numbers()
    exist = 'False'
    for num in numbers:
        num = num.lower()
        if num == number:
            exist = 'True'
    if exist == 'False':
        raise validators.ValidationError(
            'digite un número valido (One, TwentyOne)'
            )


class sumaForm(Form):
    first_number = StringField('Text number one', [
        validators.Required(message='Número es requerido!'),
        field_text, field_exist
    ])
    second_number = StringField('Text number two', [
        validators.Required(message='Número es requerido!'),
        field_text, field_exist
    ])
    honeypot = HiddenField('', [length_honeypot])
