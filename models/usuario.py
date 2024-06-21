from . import db

class Usuario(db.Model):
    __tablename__ = 'USUARIOS'
    id = db.Column('USU_ID', db.Integer, primary_key=True)
    nome = db.Column('USU_NOME', db.String(100))
    email = db.Column('USU_EMAIL', db.String(100))
    senha = db.Column('USU_SENHA', db.String(100))
