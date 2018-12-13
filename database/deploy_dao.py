import yaml

from model.model_deploy import Deploy
from connection.mysql_conn import MysqlConnection

class DeployDao():
    
    def inserir_registro(self, model_deploy):
        print(model_deploy.versao)
        configs = yaml.load(open('config.yml'))
        conn = MysqlConnection(host=configs['database']['host'], user=configs['database']['user'], password=configs['database']['pass'], db=configs['database']['schema'])
        session = conn.connect_mysql()
        print (session)
        if session:
            query = "INSERT INTO teste_deploy (componente, versao, responsavel, status, data)  \
                VALUES('{}', '{}', '{}', '{}', '2017-06-15')".format(model_deploy.componente, model_deploy.versao, model_deploy.responsavel, model_deploy.status)
            print (query)
            try:
                result_proxy = session.execute(query)
                session.commit()
                return True
            except Exception as e:
                print (e)
                return False