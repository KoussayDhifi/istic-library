from flask import Blueprint,render_template

view = Blueprint('view',__name__,template_folder='template_view',static_folder='static_view')


@view.route("/about")
def about():
    return render_template("about.html")

