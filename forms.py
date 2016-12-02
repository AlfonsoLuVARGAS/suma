"""forms.py file."""
from wtforms import Form, StringField, validators, HiddenField

numbers = [
    "Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty", "TwentyOne", "TwentyTwo", "TwentyThree", "TwentyFour", "TwentyFive", "TwentySix", "TwentySeven", "TwentyEight", "TwentyNine", "Thirty", "ThirtyOne", "ThirtyTwo", "ThirtyThree", "ThirtyFour", "ThirtyFive", "ThirtySix", "ThirtySeven", "ThirtyEight", "ThirtyNine", "Forty", "FortyOne", "FortyTwo", "FortyThree", "FortyFour", "FortyFive", "FortySix", "FortySeven", "FortyEight", "FortyNine", "Fifty", "FiftyOne", "FiftyTwo", "FiftyThree", "FiftyFour", "FiftyFive", "FiftySix", "FiftySeven", "FiftyEight", "FiftyNine", "Sixty", "SixtyOne", "SixtyTwo", "SixtyThree", "SixtyFour", "SixtyFive", "SixtySix", "SixtySeven", "SixtyEight", "SixtyNine", "Seventy", "SeventyOne", "SeventyTwo", "SeventyThree", "SeventyFour", "SeventyFive", "SeventySix", "SeventySeven", "SeventyEight", "SeventyNine", "Eighty", "EightyOne", "EightyTwo", "EightyThree", "EightyFour", "EightyFive", "EightySix", "EightySeven", "EightyEight", "EightyNine", "Ninety", "NinetyOne", "NinetyTwo", "NinetyThree", "NinetyFour", "NinetyFive", "NinetySix", "NinetySeven", "NinetyEight", "NinetyNine", "One hundred"
]


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
