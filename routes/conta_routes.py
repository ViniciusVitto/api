from flask import Blueprint, request, jsonify
from flasgger import swag_from
from models import db
from models.conta import Conta
from schemas.conta_schemas import conta_schema, contas_schema
from utils.auth import token_required

conta_bp = Blueprint('conta_bp', __name__)

@conta_bp.route('contas/<int:id>', methods=['GET'])
@token_required
def get_conta_by_id(current_user, id):  
    conta = Conta.query.filter_by(id=id, usuario_id=current_user.id).first()
    if not conta:
        return jsonify({'message': 'Conta não encontrada'}), 404

    return conta_schema.jsonify(conta)

@conta_bp.route('/contas', methods=['GET'])
@token_required
@swag_from({
    'tags': ['Contas'],
    'description': 'Obtém todas as contas do usuário logado',
    'security': [{"Bearer": []}],
    'responses': {
        '200': {
            'description': 'Lista de contas',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'nome': {'type': 'string'},
                        'valor': {'type': 'number'},
                        'datavenc': {'type': 'string', 'format': 'date'},
                        'pago': {'type': 'string', 'enum': ['SIM', 'NAO']},
                        'usuario_id': {'type': 'integer'}
                    }
                }
            }
        }
    }
})
def get_contas(current_user):
    query = request.args.get('q')
    if query:
        contas = Conta.query.filter(Conta.nome.like(f'%{query}%'), Conta.usuario_id == current_user.id).all()
    else:
        contas = Conta.query.filter_by(usuario_id=current_user.id).all()
    return contas_schema.jsonify(contas)

@conta_bp.route('/contas', methods=['POST'])
@token_required
@swag_from({
    'tags': ['Contas'],
    'description': 'Cria uma nova conta',
    'security': [{"Bearer": []}],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string'},
                    'valor': {'type': 'number'},
                    'datavenc': {'type': 'string', 'format': 'date'},
                    'pago': {'type': 'string', 'enum': ['SIM', 'NAO']},
                    'usuario_id': {'type': 'integer'}
                },
                'required': ['nome', 'valor', 'datavenc', 'pago', 'usuario_id']
            }
        }
    ],
    'responses': {
        '201': {
            'description': 'Conta criada com sucesso'
        }
    }
})
def create_conta(current_user):
    data = request.get_json()
    new_conta = Conta(
        nome=data['nome'],
        valor=data['valor'],
        datavenc=data['datavenc'],
        pago=data['pago'],
        usuario_id=current_user.id
    )
    db.session.add(new_conta)
    db.session.commit()
    return conta_schema.jsonify(new_conta), 201

@conta_bp.route('/contas/<int:id>', methods=['DELETE'])
@token_required
@swag_from({
    'tags': ['Contas'],
    'description': 'Deleta uma conta existente',
    'security': [{"Bearer": []}],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'required': True,
            'type': 'integer'
        }
    ],
    'responses': {
        '200': {
            'description': 'Conta excluída com sucesso'
        },
        '404': {
            'description': 'Conta não encontrada'
        }
    }
})
def delete_conta(current_user, id):
    conta = Conta.query.filter_by(id=id, usuario_id=current_user.id).first()
    if not conta:
        return jsonify({'message': 'Conta não encontrada'}), 404
    db.session.delete(conta)
    db.session.commit()
    return jsonify({'message': 'Conta excluída com sucesso'}), 200

@conta_bp.route('/contas/<int:id>', methods=['PUT'])
@token_required
@swag_from({
    'tags': ['Contas'],
    'description': 'Atualiza uma conta existente',
    'security': [{"Bearer": []}],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'required': True,
            'type': 'integer'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string'},
                    'valor': {'type': 'number'},
                    'datavenc': {'type': 'string', 'format': 'date'},
                    'pago': {'type': 'string', 'enum': ['SIM', 'NAO']}
                }
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'Conta atualizada com sucesso'
        },
        '404': {
            'description': 'Conta não encontrada'
        }
    }
})
def update_conta(current_user, id):
    conta = Conta.query.filter_by(id=id, usuario_id=current_user.id).first()
    if not conta:
        return jsonify({'message': 'Conta não encontrada'}), 404

    data = request.get_json()
    conta.nome = data.get('nome', conta.nome)
    conta.valor = data.get('valor', conta.valor)
    conta.datavenc = data.get('datavenc', conta.datavenc)
    conta.pago = data.get('pago', conta.pago)
    db.session.commit()


    return conta_schema.jsonify(conta)
