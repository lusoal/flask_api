import json

from model.model_deploy import Deploy
from database.deploy_dao import DeployDao

class DeployController():

    def __init__(self):
        self.dao = DeployDao()
    
    def insert_deploy(self, deploy):
        if not None in deploy.to_list():
            return self.dao.inserir_registro(deploy)
        else:
            print ('Parametros passados no POST sao invalidos')
            return False
    
    def select_all_deploys(self):
        result = self.dao.select_all()
        list_of_values = []
        if result:
            for values in result:
                dict_return = {'ID': None, 'Componente': None, 'Versao': None, 'Responsavel': None, 'Status': None, 'Data': None}
                dict_return['ID'] = values[0]
                dict_return['Componente'] = values[1]
                dict_return['Versao'] = values[2]
                dict_return['Responsavel'] = values[3]
                dict_return['Status'] = values[4]
                dict_return['Data'] = values[5]
                list_of_values.append(dict_return)
            return list_of_values
        else:
            return False
    
    def select_some_deploy(self, coluna, valor):
        result = self.dao.select_some_deploy(coluna, valor)
        list_of_values = []
        print (result)
        if result:
            for values in result:
                dict_return = {'ID': None, 'Componente': None, 'Versao': None, 'Responsavel': None, 'Status': None, 'Data': None}
                dict_return['ID'] = values[0]
                dict_return['Componente'] = values[1]
                dict_return['Versao'] = values[2]
                dict_return['Responsavel'] = values[3]
                dict_return['Status'] = values[4]
                dict_return['Data'] = values[5]
                list_of_values.append(dict_return)
            return list_of_values
        else:
            return False
    
    def mock_deploy_test(self):
        list_of_values = []
        result = [[00, 'Testing', 'Teste', 'Pytest', True, '02-10-1997']]
        if result:
            for values in result:
                dict_return = {'ID': None, 'Componente': None, 'Versao': None, 'Responsavel': None, 'Status': None, 'Data': None}
                dict_return['ID'] = values[0]
                dict_return['Componente'] = values[1]
                dict_return['Versao'] = values[2]
                dict_return['Responsavel'] = values[3]
                dict_return['Status'] = values[4]
                dict_return['Data'] = values[5]
                list_of_values.append(dict_return)
            return list_of_values
        else:
            return False
        