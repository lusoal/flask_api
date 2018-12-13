from sqlalchemy import *
from sqlalchemy.orm import *

class MysqlConnection:

    def __init__(self, host, user, password, db):
        self.user = user
        self.host = host
        self.password = password
        self.db = db
        

    def connect_mysql(self):
        #connection db
        try:
            engine = create_engine("mysql://"+self.user+":"+self.password+"@"+self.host+"/"+self.db)
            #creating session
            Session = sessionmaker()
            Session.configure(bind=engine)
            session = Session()
            return session
        except Exception as e:
            print (e)
            return False

        #stmt = query
        #try:
        #    result_proxy = session.execute(stmt)
        #    if 'INSERT' in stmt or 'UPDATE' in stmt or 'DELETE' in stmt:
        #        session.commit()
        #        return True
#
        #    if 'SELECT' in stmt:
        #        result = result_proxy.fetchall()
        #        return result
#
        #except Exception as e:
        #    print  (e)
        #    if '_mysql_exceptions.IntegrityError' in str(e):
        #        return "Already here"
        #    else:
        #        return False
