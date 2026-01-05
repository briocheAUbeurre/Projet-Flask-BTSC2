from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def accueil():
    return "Serveur Flask OK (Windows + VS Code)"

@app.route("/bjr")
def bjr():
    return render_template("bjr.html")

@app.route("/ping/<username>")
def ping(username):
    return f'bonjour {escape(username)}'

@app.route("/ping2/<username>")
def ping2(username):
    return render_template("bjr.html", username=username)


app.run(host="0.0.0.0", port=5000)
