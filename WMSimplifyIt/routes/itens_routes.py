from flask import *
from classes.itens import Itens
blue_itens = Blueprint("itens",__name__,template_folder = "templates")

@blue_itens.route("/add_item", methods = ["GET","POST"])
def add_item():
    if "User" in session:
        if request.method == "GET":
            return render_template("add_item.html")
        else:
            nome = request.form["name"]
            quantity = request.form["quantity"]
            price = request.form["price"]
            i1 = Itens()
            i1.add_new(nome,quantity,price)
            return redirect("/itens/viewall_item")
    else:
        return redirect("/funcionarios/login")

@blue_itens.route("/update_item/<_id_>", methods = ["GET","POST"])
def update_item(_id_):
    if "User" in session:
        if request.method == "GET":
            f1 = Itens()
            return render_template("update_item.html", dados = f1.view_one(_id_))

        else:
            nome = request.form["name"]
            quantity = request.form["quantity"]
            price = request.form["price"]
            f1 = Itens()
            f1.update(nome,quantity,price,_id_)
            return redirect("/itens/viewone_item/" + _id_ + "")
    else:
        return redirect("/funcionarios/login")

@blue_itens.route("/delete_item/<_id_>", methods = ["GET", "POST"])
def delete_item(_id_):
    if "User" in session:
        if request.method == "GET":
            f1 = Itens()
            return render_template("delete_item.html", dados = f1.view_one(_id_))
        else:
            f1 = Itens()
            f1.delete(_id_)
            return redirect("/itens/viewall_item")
    else:
        return redirect("/funcionarios/login")

@blue_itens.route("/viewall_item", methods = ["GET","POST"])
def viewall_item():
    #if "User" in session:
        f1 = Itens()
        return render_template("viewall_item.html", dados = f1.view_all())
    #else:
        return redirect("/funcionarios/login")

@blue_itens.route("/viewone_item/<_id_>", methods = ["GET"])
def viewone_item(_id_):
    if "User" in session:
        f1 = Itens()
        return render_template("viewone_item.html", dados = f1.view_one(_id_))
    else:
        return redirect("/funcionarios/login")
