from flask import Blueprint,render_template

view = Blueprint(__name__,template_folder=template_view,static_folder=static_view)


@view.route("/upload")
def upload():
    return render_template("upload.html")
