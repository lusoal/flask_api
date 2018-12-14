from datetime import datetime

class Deploy():
    def __init__(self, componente=None, versao=None, responsavel=None, status=None, id=None, data=None):
        self.componente = componente
        self.versao = versao
        self.responsavel = responsavel
        self.status = status
        self.id = id
        self.data= (datetime.now()).strftime('%Y-%m-%d %H:%M:%S')

    def to_list(self):
        list_return = [
          self.componente, 
          self.versao, 
          self.responsavel, 
          self.status ]
        return list_return
        