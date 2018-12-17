import yaml
import os

from model.model_deploy import Deploy
from connection.mysql_conn import MysqlConnection

class DeployDao():

    def inserir_registro(self, model_deploy):
        print(model_deploy.versao)
        conn = MysqlConnection(host=os.getenv('DB_HOST', 'host_db'), user=os.getenv('DB_USER', 'user_db'), password=os.getenv('DB_PASS', 'pass_db'), db=os.getenv('DB_SCHEMA', 'schema_db'))
        session = conn.connect_mysql()
        print (session)
        if session:
            print (model_deploy.data)
            query = "INSERT INTO teste_deploy (componente, versao, responsavel, status, data)  \
                VALUES('{}', '{}', '{}', '{}', '{}')".format(model_deploy.componente, model_deploy.versao, model_deploy.responsavel, model_deploy.status, model_deploy.data)
            print (query)
            try:
                result_proxy = session.execute(query)
                session.commit()
                return True
            except Exception as e:
                print (e)
                return False
    
    def select_all(self):
        conn = MysqlConnection(host=os.getenv('DB_HOST', 'host_db'), user=os.getenv('DB_USER', 'user_db'), password=os.getenv('DB_PASS', 'pass_db'), db=os.getenv('DB_SCHEMA', 'schema_db'))
        session = conn.connect_mysql()
        query = "SELECT * FROM teste_deploy"
        if session:
            try:
                result_proxy = session.execute(query)
                result = result_proxy.fetchall()
                return result
            except Exception as e:
                print (e)
                return False
    
    def select_some_deploy(self, coluna, valor):
        conn = MysqlConnection(host=os.getenv('DB_HOST', 'host_db'), user=os.getenv('DB_USER', 'user_db'), password=os.getenv('DB_PASS', 'pass_db'), db=os.getenv('DB_SCHEMA', 'schema_db'))
        session = conn.connect_mysql()
        query = "SELECT * from teste_deploy WHERE {} LIKE {}".format(coluna, valor)
        if session:
            try:
                result_proxy = session.execute(query)
                result = result_proxy.fetchall()
                return result
            except Exception as e:
                print (e)
                return False