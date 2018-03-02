from flask import *
from classes.pedidos import Pedidos
from classes.itens import Itens
from classes.clientes import Clientes
import datetime
blue_pedidos = Blueprint("pedidos",__name__,template_folder = "templates")


@blue_pedidos.route("/add_pedido",methods = ["GET","POST"])
def add_pedido():
#    if "User" in session:
    if request.method == "GET":
        i1 = Itens()
        c1 = Clientes()
        return render_template("add_pedido.html",dados_clientes = c1.view_all(),dados = i1.view_all())
    else:
        data = datetime.datetime.today().strftime("%Y-%m-%d")
        itens = request.get_json()
        status = True
        customer = itens["customer"]
        itens = itens["items"]
        p1 = Pedidos()
        p1.add_new(data,customer,status)
        id_pedido = p1.get_id(data,customer,status)
        print(id_pedido)
        for item in itens:
            print(item)
            _id_ = item["id"]
            nome = item["name"]
            price = item["price"]
            quantity = item["quantity"]
            ip1 = Itens_Pedidos()
            ip1.add_new(data,nome,quantity,price,_id_,id_pedido)
            print("ok5")
            session["Carrinho"] = itens       
            #p1 = Pedidos()
            #p1.add_new(customer,status,itens)
            #print(id,nome,customer)
        msg = {"msg":"OK"}
        #MSG -> LINK PEDIDO OU CONTINUAR COMPRANDO
        return json.dumps(msg) 
            #redirect("/pedidos/viewall_pedidos")
    #else:
    #    return redirect("/funcionarios/login")

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