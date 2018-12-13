from flask import Flask, jsonify, request

from model.model_deploy import Deploy
from controller.deploy_controller import DeployController

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/cadastrar_deploy', methods=['POST'])
def save_to_db():
    content = request.get_json()
    if len(content) == 4:
        model = Deploy(content.get('componente'), content.get('versao'), content.get('responsavel'), content.get('status'))
        controller = DeployController(model)
        return jsonify(controller.insert_deploy())
    
if __name__ == '__main__':
    app.run(debug=True)
