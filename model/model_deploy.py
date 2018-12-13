class Deploy():

    def __init__(self, componente=None, versao=None, responsavel=None, status=None, id=None):
        self.componente = componente
        self.versao = versao
        self.responsavel = responsavel
        self.status = status
        self.id = id

    def to_list(self):
        list_return = [
          self.componente, 
          self.versao, 
          self.responsavel, 
          self.status ]
        return list_return
        