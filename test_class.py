from controller.deploy_controller import DeployController
from connection.mysql_conn import MysqlConnection
import pytest

class TestClass(object):
    
    def test_dict_deploy(self):
        controller = DeployController()
        result = controller.mock_deploy_test()
        #Teste para verificar se o resultado esperado e um dicionario de valores
        print (result[0]['Status'])
        assert result[0]['Status'] == True

    def test_error_connecting(self):
        #Erro na conexao com o Mysql
        conn = MysqlConnection('teste', 'teste', 'teste', 'teste')
        session = conn.connect_mysql()
        query = "SELECT * FROM teste_deploy"
        
        with pytest.raises(Exception):
            session.execute(query)
