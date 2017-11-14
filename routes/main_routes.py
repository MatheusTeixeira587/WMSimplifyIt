from flask import *
from flask.sessions import SessionInterface
from beaker.middleware import SessionMiddleware

blue_main = Blueprint("site",__name__, template_folder = "templates")

@blue_main.route("/")
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template("home.html")

@blue_main.route('/login', methods=['POST'])
def do_admin_login():
    nome = request.form['nome']
    password = request.form['password']
    u1 = Users()
    dados = u1.view_one(nome,password)
    if nome == dados[1] and password == dados[2]:
        app_session = app.request.environ.get('beaker.session')
        session['logged_in'] = True
        return redirect("home.html")
    else:
        flash('wrong password!')
    return home()

@blue_main.route("/funcionarios/")
def funcionarios():
    return render_template("funcionarios.html")

@blue_main.route("/about")
def about():
    return render_template("about.html")

@blue_main.route("/itens/")
def itens():
    return render_template("produtos.html")

@blue_main.route("/pedidos")
def pedidos():
    return render_template("pedidos.html/")
