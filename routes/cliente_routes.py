from flask import *
from classes.clientes import Clientes
import bcrypt
blue_clientes = Blueprint("clientes",__name__,template_folder = "templates")

@blue_clientes.route("/add_clientes", methods = ["GET","POST"])
def add_clientes():
    if "User" in session:
        if request.method == "GET":
            return render_template("add_clientes.html")
        else:
            nome = request.form["nome"]
            CNPJ = request.form["CNPJ"]
            c1 = Clientes()
            c1.add_new(nome,CNPJ)
            return redirect("/clientes/viewall_clientes")
    else:
        return redirect("/funcionarios/login")

@blue_clientes.route("/update_clientes/<_id_>", methods = ["GET","POST"])
def update_clientes(_id_):
    c1 = Clientes()
    if "User" in session:
        if request.method == "GET":
            return render_template("update_clientes.html", dados = c1.view_one(_id_))
        else:
            nome = request.form["nome"]
            CNPJ = request.form["CNPJ"]            
    else:
        return redirect("/funcionarios/login")

@blue_clientes.route("/delete_clientes/<_id_>", methods = ["GET", "POST"])
def delete_clientes(_id_):
    c1 = Clientes()
    if "User" in session:
        if request.method == "GET":
            return render_template("delete_clientes.html", dados = c1.view_one(_id_))
        else:
            c1.delete(_id_)
            return redirect("/clientes/viewall_clientes")
    else:
        return redirect("funcionarios/login")

@blue_clientes.route("/viewall_clientes", methods = ["GET","POST"])
def viewall_clientes():
    c1 = Clientes()
    if "User" in session:
        return render_template("viewall_clientes.html", dados = c1.view_all())
    else:
        return redirect("/funcionarios/login")

@blue_clientes.route("/viewone_clientes/<_id_>", methods = ["GET"])
def viewone_clientes(_id_):
    c1 = Clientes()
    if "User" in session:
        return render_template("viewone_clientes.html", dados = c1.view_one(_id_))
    else:
        return redirect("/funcionarios/login")