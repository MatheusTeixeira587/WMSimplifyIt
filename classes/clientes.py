import sqlite3

class Clientes():

    def __init__(self,nome = "", CNPJ = "",table = "cliente"):
        self.table = table
        self.nome = nome
        self.CNPJ = CNPJ

    def add_new(self,nome,CNPJ):
        conn = sqlite3.connect("projetowms.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO " + self.table + " (nome,CNPJ) VALUES (?,?)",(nome,CNPJ))
        conn.commit()
        conn.close()

    def view_all(self):
        conn = sqlite3.connect("projetowms.db")
        cur = conn.cursor()
        dados = cur.execute("SELECT * FROM " + self.table).fetchall()
        conn.commit()
        conn.close()
        return dados

    def view_one(self,_id_):
        conn = sqlite3.connect("projetowms.db")
        cur = conn.cursor()
        dados = cur.execute("SELECT * FROM " + self.table + " WHERE id = ?",(_id_,)).fetchone()
        conn.close()
        return dados

    def update(self,_id_,nome = "",CNPJ = ""):
        conn = sqlite3.connect("projetowms.db")
        cur = conn.cursor()
        cur.execute("UPDATE " + self.table + " SET nome = ?, CNPJ = ?, WHERE id = ?",(nome,CNPJ,_id_))
        conn.commit()
        conn.close()

    def delete(self,_id_):
        conn = sqlite3.connect("projetowms.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM " + self.table + " WHERE id = ?",(_id_,))
        conn.commit()
        conn.close()