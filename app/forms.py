from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class CursoForm(FlaskForm):
    nome = StringField('Nome do Curso', validators=[DataRequired(), Length(min=2, max=100)])
    descricao = TextAreaField('Descrição', validators=[DataRequired(), Length(min=5, max=250)])
    submit = SubmitField('Salvar Curso')