from flask import Flask,render_template
from views.views import view
app = Flask(__name__)
app.register_blueprint(view,url_prefix="/")

@app.route("/")
def home():
    return render_template('base.html')


if "__main__" == __name__:
    app.run(debug=True)