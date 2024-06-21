from flask import Flask, send_from_directory
from flasgger import Swagger
from config import Config
from models import db
from schemas import ma
from routes import usuario_bp, conta_bp
from swagger import swagger_template, swagger_config 

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
ma.init_app(app)

app.register_blueprint(usuario_bp, url_prefix='/api')
app.register_blueprint(conta_bp, url_prefix='/api')

swagger = Swagger(app, config=swagger_config, template=swagger_template)

@app.route('/')
def serve_index():
    return send_from_directory('../front-end-billmanager', 'login.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('../front-end-billmanager', path)

def create_tables_if_not_exist():
    with app.app_context():
        db.create_all()

app.before_request(create_tables_if_not_exist)

if __name__ == '__main__':
    app.run(debug=True)
