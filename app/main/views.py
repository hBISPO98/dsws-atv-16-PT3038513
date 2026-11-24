from datetime import datetime
from flask import render_template, redirect, url_for, flash
from . import main
from .. import db
from ..models import Curso
from ..forms import CursoForm

@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

@main.route('/cursos', methods=['GET', 'POST'])
def cursos():
    form = CursoForm()
    if form.validate_on_submit():
        curso = Curso(nome=form.nome.data, descricao=form.descricao.data)
        db.session.add(curso)
        db.session.commit()
        flash('Curso cadastrado com sucesso!')
        return redirect(url_for('main.cursos'))
    
    # Busca todos os cursos cadastrados para exibir na tabela
    cursos_cadastrados = Curso.query.all()
    return render_template('cursos.html', form=form, cursos=cursos_cadastrados)

# Stubs para as outras abas do menu (conforme a avaliação)
@main.route('/professores')
def professores():
    return render_template('nao_disponivel.html')

@main.route('/disciplinas')
def disciplinas():
    return render_template('nao_disponivel.html')

@main.route('/alunos')
def alunos():
    return render_template('nao_disponivel.html')

@main.route('/ocorrencias')
def ocorrencias():
    return render_template('nao_disponivel.html')