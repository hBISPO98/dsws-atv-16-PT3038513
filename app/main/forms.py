from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class NameForm(FlaskForm):
    name = StringField('Qual o seu nome?', validators=[DataRequired()])
    submit = SubmitField('Enviar')


class CursoForm(FlaskForm):
    nome = StringField('Qual é o nome do curso?', validators=[DataRequired(), Length(1, 100)])
    descricao = TextAreaField('Descrição (250 caracteres)', validators=[DataRequired(), Length(1, 250)])
    submit = SubmitField('Cadastrar')