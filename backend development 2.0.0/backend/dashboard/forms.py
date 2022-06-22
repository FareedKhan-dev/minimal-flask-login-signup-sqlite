from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileField, FileAllowed
from wtforms import SubmitField
from wtforms import ValidationError


class uploadfile(FlaskForm):
    data = FileField(validators=[FileRequired(),FileAllowed(['csv', 'Please Upload csv only!'])])
    submit = SubmitField('Submit')
    