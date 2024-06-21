from flask import Blueprint, request, jsonify
from flasgger import swag_from
from models import db
from models.usuario import Usuario
from schemas.usuario_schemas import usuario_schema, usuarios_schema
from utils.auth import generate_token, token_required

usuario_bp = Blueprint('usuario_bp', __name__)

@usuario_bp.route('/usuarios', methods=['POST'])
@swag_from({
    'tags': ['Usuários'],
    'description': 'Cria um novo usuário',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string'},
                    'email': {'type': 'string'},
                    'senha': {'type': 'string'}
                },
                'required': ['nome', 'email', 'senha']
            }
        }
    ],
    'responses': {
        '201': {
            'description': 'Usuário criado com sucesso'
        }
    }
})
def create_usuario():
    data = request.get_json()
    new_user = Usuario(nome=data['nome'], email=data['email'], senha=data['senha'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Usuário criado com sucesso!"}), 201

@usuario_bp.route('/login', methods=['POST'])
@swag_from({
    'tags': ['Usuários'],
    'description': 'Realiza login de um usuário',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'email': {'type': 'string'},
                    'senha': {'type': 'string'}
                },
                'required': ['email', 'senha']
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'Login realizado com sucesso'
        },
        '401': {
            'description': 'Falha no login'
        }
    }
})
def login():
    data = request.get_json()
    user = Usuario.query.filter_by(email=data['email']).first()
    if user and user.senha == data['senha']:
        token = generate_token(user)
        return jsonify({'token': token}), 200
    return jsonify({'message': 'Login failed!'}), 401
