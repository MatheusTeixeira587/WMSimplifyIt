import os
from flask import *
from flask.sessions import SessionInterface
import sqlite3
from classes.funcionario import Funcionario
from classes.itens import Itens
from routes.main_routes import blue_main
from routes.funcio_routes import blue_funcio
from routes.itens_routes import blue_itens
from beaker.middleware import SessionMiddleware

session_opts = {
    'session.type': 'ext:memcached',
    'session.url': '127.0.0.1:11211',
    'session.data_dir': './cache',
}

class BeakerSessionInterface(SessionInterface):
    def open_session(self, app, request):
        session = request.environ['beaker.session']
        return session

    def save_session(self, app, session, response):
        session.save()


app = Flask(__name__, template_folder = "templates")
app.register_blueprint(blue_main)
app.register_blueprint(blue_funcio, url_prefix = "/funcionarios")
app.register_blueprint(blue_itens,url_prefix = "/itens")

def create_table():
    conn = sqlite3.connect("projetowms.db")
    #conn = psycopg2.connect("dbname = 'projetowms' user = 'postgres' password = 'postgres' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS item (id INTEGER PRIMARY KEY, nome TEXT, quantity INTEGER, price REAL)")
    cur.execute("CREATE TABLE IF NOT EXISTS func (id INTEGER PRIMARY KEY,nome TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS pedido (id INTEGER PRIMARY KEY,nome TEXT, status BOOLEAN, itens TEXT)")
    cur.execute("INSERT INTO item (nome,quantity,price) VALUES (?,?,?)",('exemplo',10,10.89))
    cur.execute("INSERT INTO func (nome )VALUES (?)",('exemplo',))
    cur.execute("INSERT INTO users (username,password) VALUES (?,?)",('matheus','123'))

    conn.commit()
    conn.close()


#create_table()
if __name__ == "__main__":
    app.wsgi_app = SessionMiddleware(app.wsgi_app, session_opts)
    app.session_interface = BeakerSessionInterface()
    app.run(debug = True)
