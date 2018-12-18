import os
import yaml
from flask import Flask, jsonify, request
from flask_selfdoc import Autodoc
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

from model.model_deploy import Deploy
from model.model_user import User
from controller.deploy_controller import DeployController

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'devops'
jwt = JWTManager(app)
auto = Autodoc(app)

@app.route('/')
@auto.doc()
def index():
    return "check for /api/help"

#Exemplo de usuario, poderia pegar o usuario do banco de dados utilizando a camada DAO, esta utilizando de um arquivo Yaml ou de variavel de ambiente
configs = yaml.load(open('config.yml'))
@app.route('/api/auth', methods=['POST'])
@auto.doc()
def login():
    """
    POST: Retorna o token para realizar as chamadas e verificar os deploys
    Exemplo: curl -XPOST https://deployment-api.lucasduarte.club/api/auth -H 'content-type: application/json' --data '{"username":"your_user", "password":"your_pass"}' 
    """
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400
    if username != os.getenv('APP_USER', configs['user']['username']) or password != str(os.getenv('APP_PASS', configs['user']['password'])):
       return jsonify({"msg": "Bad username or password"}), 401
    
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200
    

@app.route('/api/deploys', methods=['POST', 'GET'])
@auto.doc()
@jwt_required
def save_to_db():
    """
    GET: Retorna os deploys cadastrados na base de dados. 
    Exemplo: curl -XGET https://deployment-api.lucasduarte.club/api/deploys  -H 'content-type: application/json' -H 'Authorization: Bearer autorization-token'

    POST: Cadastra novo log de deploy na base de dados
    Exemplo: curl -XPOST https://deployment-api.lucasduarte.club/api/deploys -H 'content-type: application/json' -H 'Authorization: Bearer autorization-token' --data '{"componente":"teste", "versao":"01","responsavel":"teste","status":"In Progress"}' 
    """
    controller = DeployController()
    if request.method == 'POST':
        content = request.get_json()
        model = Deploy(content.get('componente'), content.get('versao'), content.get('responsavel'), content.get('status'))
        return jsonify({'Response':controller.insert_deploy(model)})
    else:
        qtd = request.args.get('qtd')
        coluna = request.args.get('coluna')
        valor = request.args.get('valor')
        if coluna:
            try:
                valor = int(valor)
            except:
                print('Not an int')
                valor = "'{}'".format(valor)
            return jsonify({'Response':controller.select_some_deploy(coluna, valor)})
        else:
            return jsonify({'Response':controller.select_all_deploys(qtd)})
        


@app.route('/api/deploys/<id>', methods=['GET'])
@auto.doc()
@jwt_required
def consult_deploy(id):
    """

    GET: Retorna os deploys cadastrados na base de dados. 
    Exemplo: curl -XGET https://deployment-api.lucasduarte.club/api/deploys/20  -H 'content-type: application/json' -H 'Authorization: Bearer autorization-token'
    
    """
    coluna = 'id'
    valor = id
    try:
        valor = int(valor)
    except:
        print('Not an int')
        valor = "'{}'".format(valor)
    
    controller = DeployController()
    return jsonify({'Response':controller.select_some_deploy(coluna, valor)})

@app.route('/api/health', methods=['GET'])
@auto.doc()
def healthcheck():
    return jsonify({'Response':True})

@app.route('/api/help')
@auto.doc()
def documentation():
    return auto.html()
    
if __name__ == '__main__':
    #Host resposavel para servir o trafego alem do localhost
    app.run(debug=True, host='0.0.0.0')
