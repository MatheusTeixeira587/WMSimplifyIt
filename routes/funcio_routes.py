from flask import *
from classes.funcionario import User
import bcrypt
blue_funcio = Blueprint("func",__name__,template_folder = "templates")

@blue_funcio.route("/login", methods = ["GET","POST"])
def login_funcio():
    if request.method == "GET":
        return render_template("login_funcio.html")
    else:
        nome = request.form["nome"]
        senha =  request.form["senha"]
        u1 = User()
        if(u1.check_pass(nome,senha)):
            session["User"] = nome
            return redirect("/")
@blue_funcio.route("/add_funcio", methods = ["GET","POST"])
def add_funcio():
    u1 = User()
    if "User" in session:
        if request.method == "GET":
            return render_template("add_funcio.html")
        else:
            nome = request.form["nome"]
            senha = bcrypt.hashpw(request.form["senha"].encode("utf-8"),bcrypt.gensalt())
            u1.add_new(nome,senha)
            return redirect("/funcionarios/viewall_funcio")
    else:
        return redirect("/funcionarios/login")

@blue_funcio.route("/update_funcio/<_id_>", methods = ["GET","POST"])
def update_funcio(_id_):
    u1 = User()
    if "User" in session:
        if request.method == "GET":
            return render_template("update_funcio.html", dados = u1.view_one(_id_))
        else:
            nome = request.form["nome"]
            antiga_senha = request.form["antiga_senha"]
            nova_senha = request.form["senha"]
            confirma_nova_senha = request.form["senha2"]
            if senha == senha2:
                salt = bcrypt.gensalt()
                senha = bcrypt.hashpw(senha.encode("utf-8"),salt)
                u1 = User()
                if(u1.check_pass(_id_,antiga_senha)):
                    u1.update(nome,_id_,senha)
                    return redirect("/funcionarios/viewone_funcio/" + _id_ + "")
    else:
        return redirect("/funcionarios/login")


@blue_funcio.route("/delete_funcio/<_id_>", methods = ["GET", "POST"])
def delete_funcio(_id_):
    u1 = User()
    if "User" in session:
        if request.method == "GET":
            return render_template("delete_funcio.html", dados = u1.view_one(_id_))
        else:
            u1.delete(_id_)
            return redirect("/funcionarios/viewall_funcio")
    else:
        return redirect("funcionarios/login")

@blue_funcio.route("/viewall_funcio", methods = ["GET","POST"])
def viewall_funcio():
    u1 = User()
    if "User" in session:
        return render_template("viewall_funcio.html", dados = u1.view_all())
    else:
        return redirect("/funcionarios/login")

@blue_funcio.route("/viewone_funcio/<_id_>", methods = ["GET"])
def viewone_funcio(_id_):
    u1 = User()
    if "User" in session:
        return render_template("viewone_funcio.html", dados = u1.view_one(_id_))
    else:
        return redirect("/funcionarios/login")
