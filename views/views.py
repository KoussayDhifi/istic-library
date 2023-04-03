from flask import Blueprint,render_template

view = Blueprint('view',__name__,template_folder='template_view',static_folder='static_view')


@view.route("/about")
def about():
    return render_template("about.html")

@view.route("/login",methods=["GET","POST"])
def login():
    return render_template("login.html")

