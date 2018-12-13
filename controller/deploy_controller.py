from model.model_deploy import Deploy
from database.deploy_dao import DeployDao

class DeployController():

    def __init__(self, deploy=None):
        self.deploy = deploy
    
    def insert_deploy(self):
        if not None in self.deploy.to_list():
            dao = DeployDao()
            return dao.inserir_registro(self.deploy)
        else:
            return {'Status':False}