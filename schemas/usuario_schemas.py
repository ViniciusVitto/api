from . import ma
from models.usuario import Usuario

class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)
