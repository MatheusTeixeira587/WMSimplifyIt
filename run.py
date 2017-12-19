import os
from flask import *
from flask.sessions import SessionInterface
import sqlite3
from classes.funcionario import User
from classes.itens import Itens
from routes.main_routes import blue_main
from routes.funcio_routes import blue_funcio
from routes.itens_routes import blue_itens

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
app.register_blueprint(blue_itens,url_prefix = "/pedidos")


def create_table():
    conn = sqlite3.connect("projetowms.db")
    #conn = psycopg2.connect("dbname = 'projetowms' user = 'postgres' password = 'postgres' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS item (id INTEGER PRIMARY KEY, nome TEXT, quantity INTEGER, price REAL)")
    cur.execute("CREATE TABLE IF NOT EXISTS func (id INTEGER PRIMARY KEY,nome TEXT,senha TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS pedido (id INTEGER PRIMARY KEY,nome TEXT, status BOOLEAN, itens TEXT)")
    cur.execute("INSERT INTO item (nome,quantity,price) VALUES (?,?,?)",('exemplo',10,10.89))
    cur.execute("INSERT INTO func (nome,senha )VALUES (?,?)",('matheus','123'))

    conn.commit()
    conn.close()


#create_table()
if __name__ == "__main__":
    app.run(debug = True)
