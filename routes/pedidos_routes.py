from flask import *
from classes.pedidos import Pedidos
blue_pedidos = Blueprint("pedidos",__name__,template_folder = "templates")

@blue_pedidos.route("/add_pedido",methods = ["GET","POST"])
def add_pedido():
    if request.method == "GET":
        return render_template("add_pedido.html")
    else:
        nome = request.form["name"]
        itens = request.form["itens"]
        status = True
        p1 = Pedidos()
        p1.add_new(nome,status,itens)
        return redirect("/pedidos/viewall_pedidos")

@blue_pedidos.route("/update_pedido/<_id_>", methods = ["GET","POST"])
def update_pedido(_id_):
    if request.method == "GET":
        p1 = pedidos()
        return render_template("update_pedido.html", dados = p1.view_one(_id_))

    else:
        nome = request.form["name"]
        status = True
        itens = request.form["itens"]
        p1 = pedidos()
        p1.update(nome,status,itens,_id_)
        return redirect("/pedidos/viewone_pedido/" + _id_ + "")


@blue_pedidos.route("/delete_pedido/<_id_>", methods = ["GET", "POST"])
def delete_pedido(_id_):
    if request.method == "GET":
        p1 = pedidos()
        return render_template("delete_pedido.html", dados = p1.view_one(_id_))
    else:
        p1 = pedidos()
        p1.delete(_id_)
        return redirect("/pedidos/viewall_pedido")

@blue_pedidos.route("/viewall_pedido", methods = ["GET","POST"])
def viewall_pedido():
    p1 = pedidos()
    return render_template("viewall_pedido.html", dados = p1.view_all())

@blue_pedidos.route("/viewone_pedido/<_id_>", methods = ["GET"])
def viewone_pedido(_id_):
    p1 = pedidos()
    return render_template("viewone_pedido.html", dados = p1.view_one(_id_))
