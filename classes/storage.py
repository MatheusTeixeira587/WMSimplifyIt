import sqlite3

class Storage():

    def __init__(self,table = "storage",_id_ = "",ruas = "",prateleiras_rua = "")
        self.table = table
        self._id_ = _id_
        self.ruas = ruas
        self.prateleiras_rua = prateleiras_rua

    def add_new(self,ruas,prateleiras,andares,posicoes):
        conn = sqlite3.connect("projetowms.db")
        cur = conn.cursor()
        for ruas in self:

        conn.commit()
        conn.close()