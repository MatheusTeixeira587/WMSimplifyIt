from flask import *
from flask.sessions import SessionInterface

blue_main = Blueprint("site",__name__, template_folder = "templates")

@blue_main.route("/")
def home():
    if "User" in session:
        return render_template("home.html")
    else:
        return redirect("/funcionarios/login")

@blue_main.route("/funcionarios/")
def funcionarios():
    if "User" in session:
        return render_template("funcionarios.html")
    else:
        return redirect("/funcionarios/login")

@blue_main.route("/about")
def about():
    if "User" in session:
        return render_template("about.html")
    else:
        return redirect("/funcionarios/login")

@blue_main.route("/itens/")
def itens():
    if "User" in session:
        return render_template("produtos.html")
    else:
        return redirect("/funcionarios/login")

@blue_main.route("/pedidos")
def pedidos():
    if "User" in session:
        return render_template("pedidos.html")
    else:
        return redirect("/funcionarios/login")

@blue_main.route("/clientes")
def clientes():
    if "User" in session:
        return render_template("clientes.html")
    else:
        return redirect("/funcionarios/login")
