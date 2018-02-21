from flask import *
from classes.pedidos import Pedidos
blue_pedidos = Blueprint("pedidos",__name__,template_folder = "templates")

@blue_pedidos.route("/add_pedido",methods = ["GET","POST"])
def add_pedido(json_content = ""):
    if "User" in session:
        if request.method == "GET":
            return redirect("/itens/viewall_itens.html")
        else:
            print(json_content)
            customer = request.form["customer"]
            status = True
            p1 = Pedidos()
            p1.add_new(customer,status,itens)
            return redirect("/pedidos/viewall_pedidos")
    else:
        return redirect("/funcionarios/login")

@blue_pedidos.route("/update_pedido/<_id_>", methods = ["GET","POST"])
def update_pedido(_id_):
    if "User" in session:
        if request.method == "GET":
            p1 = Pedidos()
            return render_template("update_pedido.html", dados = p1.view_one(_id_))

        else:
            nome = request.form["name"]
            status = True
            itens = request.form["itens"]
            p1 = Pedidos()
            p1.update(nome,status,itens,_id_)
            return redirect("/pedidos/viewone_pedido/" + _id_ + "")
    else:
        return redirect("/funcionarios/login")


@blue_pedidos.route("/delete_pedido/<_id_>", methods = ["GET", "POST"])
def delete_pedido(_id_):
    if "User" in session:
        if request.method == "GET":
            p1 = Pedidos()
            return render_template("delete_pedido.html", dados = p1.view_one(_id_))
        else:
            p1 = Pedidos()
            p1.delete(_id_)
            return redirect("/pedidos/viewall_pedido")
    else:
        return redirect("/funcionarios/login")

@blue_pedidos.route("/viewall_pedido", methods = ["GET","POST"])
def viewall_pedido():
    if "User" in session:
        p1 = Pedidos()
        return render_template("viewall_pedido.html", dados = p1.view_all())
    else:
        return redirect("/funcionarios/login")

@blue_pedidos.route("/viewone_pedido/<_id_>", methods = ["GET"])
def viewone_pedido(_id_):
    if "User" in session:
        p1 = Pedidos()
        return render_template("viewone_pedido.html", dados = p1.view_one(_id_))
    else:
        return redirect("/funcionarios/login")

@blue_pedidos.route("/carrinho",methods = ["GET","POST"])
def carrinho():
    if "User" in session:
        if request.method == "GET":
            dados = "Carrinho" in session
            return render_template("carrinho.html",dados = dados)
        else:
            p1 = Pedidos()

    else:
        return redirect("/funcionarios/login")