from . import ma
from models.conta import Conta

class ContaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Conta

conta_schema = ContaSchema()
contas_schema = ContaSchema(many=True)
