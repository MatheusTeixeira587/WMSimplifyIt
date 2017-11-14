from flask import *
from classes.funcionario import Funcionario
blue_funcio = Blueprint("func",__name__,template_folder = "templates")

@blue_funcio.route("/add_funcio", methods = ["GET","POST"])
def add_funcio():
    if request.method == "GET":
        return render_template("add_funcio.html")
    else:
        nome = request.form["nome"]
        f1 = Funcionario()
        f1.add_new(nome)
        return redirect("/funcionarios/viewall_funcio")

@blue_funcio.route("/update_funcio/<_id_>", methods = ["GET","POST"])
def update_funcio(_id_):
    if request.method == "GET":
        f1 = Funcionario()
        return render_template("update_funcio.html", dados = f1.view_one(_id_))

    else:
        nome = request.form["nome"]
        f1 = Funcionario()
        f1.update(nome,_id_)
        return redirect("/funcionarios/viewone_funcio/" + _id_ + "")


@blue_funcio.route("/delete_funcio/<_id_>", methods = ["GET", "POST"])
def delete_funcio(_id_):
    if request.method == "GET":
        f1 = Funcionario()
        return render_template("delete_funcio.html", dados = f1.view_one(_id_))
    else:
        f1 = Funcionario()
        f1.delete(_id_)
        return redirect("/funcionarios/viewall_funcio")

@blue_funcio.route("/viewall_funcio", methods = ["GET","POST"])
def viewall_funcio():
    f1 = Funcionario()    
    return render_template("viewall_funcio.html", dados = f1.view_all())

@blue_funcio.route("/viewone_funcio/<_id_>", methods = ["GET"])
def viewone_funcio(_id_):
    f1 = Funcionario()
    return render_template("viewone_funcio.html", dados = f1.view_one(_id_))