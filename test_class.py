from controller.deploy_controller import DeployController
from controller.deploy_controller import DeployController
import pytest

class TestClass(object):
    
    def test_dict_deploy(self):
        controller = DeployController()
        result = controller.mock_deploy_test()
        #Teste para verificar se o resultado esperado e um dicionario de valores
        print (result[0]['Status'])
        assert result[0]['Status'] == True
