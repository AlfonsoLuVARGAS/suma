"""forms.py file."""
from wtforms import Form
from wtforms import StringField


class sumaForm(Form):
    first_name = StringField('Text number one')
    last_name = StringField('Text number two')
