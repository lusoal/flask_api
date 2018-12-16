from flask import Flask, jsonify, request

from model.model_deploy import Deploy
from controller.deploy_controller import DeployController

app = Flask(__name__)

@app.route('/')
def index():
    return "My API"


@app.route('/deploy', methods=['POST', 'GET'])
def save_to_db():
    controller = DeployController()
    if request.method == 'POST':
        content = request.get_json()
        model = Deploy(content.get('componente'), content.get('versao'), content.get('responsavel'), content.get('status'))
        return jsonify({'Response':controller.insert_deploy(model)})
    else:
        return jsonify({'Response':controller.select_all_deploys()})

@app.route('/consultar_deploy', methods=['GET'])
def consult_deploy():
    coluna = request.args.get('coluna')
    valor = request.args.get('valor')
    try:
        valor = int(valor)
    except:
        print('Not an int')
        valor = "'{}'".format(valor)
    
    controller = DeployController()
    return jsonify({'Response':controller.select_some_deploy(coluna, valor)})
    
if __name__ == '__main__':
    #Host resposavel para servir o trafego alem do localhost
    app.run(debug=True, host='0.0.0.0')
