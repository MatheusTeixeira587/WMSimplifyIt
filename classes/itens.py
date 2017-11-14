import sqlite3
class Itens():

    def __init__(self,nome = "",table = "item",quantity = "",price = ""):
        self.nome = nome
        self.table = table
        self.quantity = quantity
        self.price = price

    def add_new(self,nome,quantity,price):
        conn = sqlite3.connect("projetowms.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO " + self.table + " (nome,quantity,price) VALUES (?,?,?)",(nome,quantity,price))
        conn.commit()
        conn.close()

    def view_all(self):
        conn = sqlite3.connect("projetowms.db")
        cur = conn.cursor()
        dados = cur.execute("SELECT * FROM " + self.table).fetchall()
        conn.close()
        return dados

    def view_one(self,_id_):
        conn = sqlite3.connect("projetowms.db")
        cur = conn.cursor()
        dados = cur.execute("SELECT * FROM " + self.table + " WHERE id = ?",(_id_,)).fetchone()
        conn.close()
        return dados

    def update(self,nome,quantity,price,_id_):
        conn = sqlite3.connect("projetowms.db")
        cur = conn.cursor()
        cur.execute("UPDATE " + self.table + " SET (nome,quantity,price) WHERE id = ?",(nome,quantity,price,_id_))
        conn.commit()
        conn.close()

    def delete(self,_id_):
        conn = sqlite3.connect("projetowms.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM " + self.table + " WHERE id = ?",(_id_,))
        conn.commit()
        conn.close()
