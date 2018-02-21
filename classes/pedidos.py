import sqlite3

class Pedidos():

    def __init__(self,table = "pedido",_id_ = "", id_cliente = "",id_itens_pedidos = "",date = "", status = ""):
        self.table = table
        self.status = status
        self.id_cliente = id_cliente
        self.id_itens_pedidos = id_itens_pedidos
        self.date = date

    def add_new(self,nome,status,itens):
        conn = sqlite3.connect("projetowms.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO " + self.table + " (date,status,id_cliente,id_itens_pedidos) VALUES (?)",(date,status,id_cliente,id_itens_pedidos))
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
        cur.execute("UPDATE " + self.table + " SET date = ?, status = ?, id_cliente = ?,id_itens_pedidos = ?, WHERE id = ?",(date,status,id_cliente,id_itens_pedidos,_id_))
        conn.commit()
        conn.close()

    def delete(self,_id_):
        conn = sqlite3.connect("projetowms.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM " + self.table + " WHERE id = ?",(_id_,))
        conn.commit()
        conn.close()

    def turn_status(self,_id_):
        conn = sqlite3.connect("projetowms.db")
        cur = conn.cursor()
        status = cur.execute("SELECT status FROM " + self.table + " WHERE id = ?",(_id_,)).fetchone()
        new_status = True
        if(status == True):
            new_status = False            
        cur.execute("UPDATE " + self.table + " SET status = ? WHERE id = ?",(new_status,_id_))
        cur.commit()
        cur.close()