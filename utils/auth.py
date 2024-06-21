from functools import wraps
from flask import request, jsonify, current_app
import jwt
from models.usuario import Usuario
from models import db

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-tokens')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = Usuario.query.filter_by(id=data['id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

def generate_token(user):
    token = jwt.encode({'id': user.id}, current_app.config['SECRET_KEY'], algorithm="HS256")
    return token
