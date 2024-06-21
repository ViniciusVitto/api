# api
Esse é um Backend em Python, elaborado durante a pós graduação, com o objetivo de auxiliar no gerenciamento de contas a pagar.

---
## Como executar

Será necessário ter o Python instalado em seu ambiente e executar o seguinte comando

> Caso não tenha o Python em seu computador basta acessar: (https://marketplace.visualstudio.com/items?itemName=ms-python.python)

```
pip install Flask Flask-SQLAlchemy flask-marshmallow pyjwt marshmallow-sqlalchemy flasgger
```

Este comando instala todas as bibliotecas necessárias para executar a api.

Porém antes de executar a api é necessário ter o Frontend baixado em seu computador e o banco de dados.

> O banco de dados está em formato SQL e fica dentro da pasta database/BILLMANAGER.sql

> O Frontend é encontrado: https://github.com/ViniciusVitto/front-end-billmanager

Após o banco de dados sendo executado e o Frontend no computador basta executar o comando:

```
python app.py 
```
