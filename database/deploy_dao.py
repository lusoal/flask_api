import yaml
import os

from model.model_deploy import Deploy
from connection.mysql_conn import MysqlConnection

class DeployDao():

    def __init__(self):
        self.configs = yaml.load(open('config.yml'))

    def inserir_registro(self, model_deploy):
        print(model_deploy.versao)
        conn = MysqlConnection(host=os.getenv('DB_HOST', self.configs['database']['host']), user=os.getenv('DB_USER', self.configs['database']['user']), password=os.getenv('DB_PASS', self.configs['database']['pass']), db=os.getenv('DB_SCHEMA', self.configs['database']['schema']))
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
    
    def select_all(self, limite=None):
        conn = MysqlConnection(host=os.getenv('DB_HOST', self.configs['database']['host']), user=os.getenv('DB_USER', self.configs['database']['user']), password=os.getenv('DB_PASS', self.configs['database']['pass']), db=os.getenv('DB_SCHEMA', self.configs['database']['schema']))
        session = conn.connect_mysql()
        if limite:
            query = "SELECT * FROM teste_deploy ORDER BY id LIMIT {}".format(int(limite))
        else:
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
        conn = MysqlConnection(host=os.getenv('DB_HOST', self.configs['database']['host']), user=os.getenv('DB_USER', self.configs['database']['user']), password=os.getenv('DB_PASS', self.configs['database']['pass']), db=os.getenv('DB_SCHEMA', self.configs['database']['schema']))
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