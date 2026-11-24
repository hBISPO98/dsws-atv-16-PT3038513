from . import db


class Curso(db.Model):
    __tablename__ = 'cursos'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Curso %r>' % self.nome