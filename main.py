import os
import yaml
from flask import Flask, jsonify, request
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

from model.model_deploy import Deploy
from model.model_user import User
from controller.deploy_controller import DeployController

#Exemplo de usuario, poderia pegar o usuario do banco de dados utilizando a camada DAO, esta utilizando de um arquivo Yaml ou de variavel de ambiente
configs = yaml.load(open('config.yml'))

users = [
    User(1, os.getenv('APP_USER', configs['user']['username']), str(os.getenv('APP_PASS', configs['user']['password'])))
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'devops'
jwt = JWT(app, authenticate, identity)


@app.route('/')
def index():
    return "My API"


@app.route('/deploys', methods=['POST', 'GET'])
@jwt_required()
def save_to_db():
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
        


@app.route('/deploys/<id>', methods=['GET'])
@jwt_required()
def consult_deploy(id):
    #coluna = request.args.get('coluna')
    coluna = 'id'
    valor = id
    try:
        valor = int(valor)
    except:
        print('Not an int')
        valor = "'{}'".format(valor)
    
    controller = DeployController()
    return jsonify({'Response':controller.select_some_deploy(coluna, valor)})

@app.route('/health', methods=['GET'])
def healthcheck():
    return jsonify({'Response':True})
    
if __name__ == '__main__':
    #Host resposavel para servir o trafego alem do localhost
    app.run(debug=True, host='0.0.0.0')
