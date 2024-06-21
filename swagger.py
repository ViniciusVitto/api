swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Bill Manager API",
        "description": "API para gerenciamento de contas",
        "version": "1.0.0",
    },
    "host": "127.0.0.1:5000",
    "basePath": "/api",
    "schemes": ["http"],
    "tags": [
        {
            "name": "Usuários",
            "description": "Operações relacionadas a usuários"
        },
        {
            "name": "Contas",
            "description": "Operações relacionadas a contas"
        },
    ],
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "x-access-tokens",
            "in": "header",
            "description": "JWT Authorization header using the Bearer scheme. Example: 'Authorization: Bearer {token}'",
        }
    },
    "security": [
        {
            "Bearer": []
        }
    ]
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec_1",
            "route": "/apispec_1.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger/",
}
