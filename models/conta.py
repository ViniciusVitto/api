from . import db

class Conta(db.Model):
    __tablename__ = 'CONTAS'
    id = db.Column('CON_ID', db.Integer, primary_key=True)
    nome = db.Column('CON_NOME', db.String(100))
    valor = db.Column('CON_VALOR', db.Float)
    datavenc = db.Column('CON_DATAVENC', db.Date)
    pago = db.Column('CON_PAGO', db.Enum('SIM', 'NAO'))
    usuario_id = db.Column('FK_USUARIOS_USU_ID', db.Integer, db.ForeignKey('USUARIOS.USU_ID'))
