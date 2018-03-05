import os
from flask import *
from flask.sessions import SessionInterface
import sqlite3
from classes.funcionario import User
from classes.itens import Itens
from routes.main_routes import blue_main
from routes.funcio_routes import blue_funcio
from routes.itens_routes import blue_itens
from routes.cliente_routes import blue_clientes 
from routes.pedidos_routes import blue_pedidos
import bcrypt

session_opts = {
    'session.type': 'ext:memcached',
    'session.url': '127.0.0.1:11211',
    'session.data_dir': './cache',
}

app = Flask(__name__, template_folder = "templates")
app.secret_key = os.urandom(24)
app.register_blueprint(blue_main)
app.register_blueprint(blue_funcio, url_prefix = "/funcionarios")
app.register_blueprint(blue_itens,url_prefix = "/itens")
app.register_blueprint(blue_pedidos,url_prefix = "/pedidos")
app.register_blueprint(blue_clientes,url_prefix = "/clientes")

def create_table():
    senha = "admin"
    senhash = bcrypt.hashpw(senha.encode("utf-8"),bcrypt.gensalt())

    #conn = psycopg2.connect("dbname = 'projetowms' user = 'postgres' password = 'postgres' host = 'localhost' port = '5432'")
    conn = sqlite3.connect("projetowms.db")
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS item (id INTEGER PRIMARY KEY, nome TEXT, quantity INTEGER, price REAL, endereco TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS func (id INTEGER PRIMARY KEY,nome TEXT,senha TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS cliente (id INTEGER PRIMARY KEY, nome TEXT, CNPJ text)")
    cur.execute("CREATE TABLE IF NOT EXISTS pedido (id INTEGER PRIMARY KEY,data DATE, status BOOLEAN,id_cliente INTEGER,FOREIGN KEY (id_cliente) REFERENCES cliente(id))")
<<<<<<< HEAD
    cur.execute("CREATE TABLE IF NOT EXISTS itens_pedidos (id INTEGER PRIMARY KEY, price REAL, quantity INTEGER, nome TEXT,id_cliente INTEGER, id_produto INTEGER, FOREIGN KEY (id_produto) REFERENCES item(id), FOREIGN KEY (id_cliente) REFERENCES cliente(id))")
=======
    cur.execute("CREATE TABLE IF NOT EXISTS itens_pedidos (id INTEGER PRIMARY KEY, price REAL, quantity INTEGER, nome TEXT, id_produto INTEGER,id_pedido INTEGER, FOREIGN KEY (id_produto) REFERENCES item(id),FOREIGN KEY (id_pedido) REFERENCES pedido(id))")
>>>>>>> 0e1cc2230c3d6d66ced139d7527679d1bceb3364

    cur.execute("INSERT INTO item (nome,quantity,price) VALUES (?,?,?)",('exemplo',10,10.89))
    cur.execute("INSERT INTO func (nome,senha )VALUES (?,?)",('matheus',senhash))

    conn.commit()
    conn.close()


#create_table()
if __name__ == "__main__":
    app.run(debug = True)
