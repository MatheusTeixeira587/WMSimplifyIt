import sqlite3

class Pedidos():
	
	def __init__(self,_id_ = "", id_cliente = "",data = "", status = ""):
		self.table = table
		self.status = status
		self.itens = itens

	def add_new(self,nome,status,itens):
		conn = sqlite3.connect("projetowms.db")
		cur = conn.cursor()
		cur.execute("INSERT INTO " + self.table + " (nome,status,itens) VALUES (?)",(nome,status,itens))
		conn.commit()
		conn.close()

	def view_all(self):
        #conn = psycopg2.connect("dbname = 'projetowms' user = 'postgres' password = 'postgres' host = 'localhost' port = '5432'")
        conn = sqlite3.connect("projetowms.db")
        cur = conn.cursor()
        dados = cur.execute("SELECT * FROM " + self.table).fetchall()
        conn.close()
        return dados

    def view_one(self,_id_):
        #conn = psycopg2.connect("dbname = 'projetowms' user = 'postgres' password = 'postgres' host = 'localhost' port = '5432'")
        conn = sqlite3.connect("projetowms.db")
        cur = conn.cursor()
        dados = cur.execute("SELECT * FROM " + self.table + " WHERE id = ?",(_id_,)).fetchone()
        conn.close()
        return dados

    def update(self,nome,status,itens,_id_):
        conn = sqlite3.connect("projetowms.db")
        cur = conn.cursor()
        cur.execute("UPDATE " + self.table + " SET nome = ?, status = ?, itens = ?, WHERE id = ?",(nome,status,itens,_id_))
        conn.commit()
        conn.close()

    def delete(self,_id_):
        conn = sqlite3.connect("projetowms.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM " + self.table + " WHERE id = ?",(_id_,))
        conn.commit()
        conn.close()