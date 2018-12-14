import yaml

from model.model_deploy import Deploy
from connection.mysql_conn import MysqlConnection

class DeployDao():

    def __init__(self):
        self.configs = yaml.load(open('config.yml'))

    def inserir_registro(self, model_deploy):
        print(model_deploy.versao)
        conn = MysqlConnection(host=self.configs['database']['host'], user=self.configs['database']['user'], password=self.configs['database']['pass'], db=self.configs['database']['schema'])
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
                return {'Response': True}
            except Exception as e:
                print (e)
                return {'Response': False}
    
    def select_all(self):
        conn = MysqlConnection(host=self.configs['database']['host'], user=self.configs['database']['user'], password=self.configs['database']['pass'], db=self.configs['database']['schema'])
        session = conn.connect_mysql()
        query = "SELECT * FROM teste_deploy"
        if session:
            try:
                result_proxy = session.execute(query)
                result = result_proxy.fetchall()
                return result
            except Exception as e:
                print (e)
                return {'Response' : False}
        