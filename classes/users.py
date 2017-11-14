import sqlite3
class Users():

    def __init__(self,nome = "",password = ""):
        self.nome = nome
        self.password = password

    def add_new(self,nome,password):
        conn = sqlite3.connect("projetowms.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO " + self.table + " (nome,password) VALUES (?,?)",(nome,password))
        conn.commit()
        conn.close()

    def view_one(self,nome,password):
        conn = sqlite3.connect("projetowms.db")
        cur = conn.cursor()
        dados = cur.execute("SELECT * FROM " + self.table + " WHERE nome = ? or password = ?",(nome,password)).fetchone()
        conn.close()
        return dados

    def update(self,nome,quantity,price,_id_):
        conn = sqlite3.connect("projetowms.db")
        cur = conn.cursor()
        cur.execute("UPDATE " + self.table + " SET (nome,password) WHERE id = ?",(nome,password,price,_id_))
        conn.commit()
        conn.close()

    def delete(self,_id_):
        conn = sqlite3.connect("projetowms.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM " + self.table + " WHERE id = ?",(_id_,))
        conn.commit()
        conn.close()
