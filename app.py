from datetime import date
from datetime import datetime

from flask import Flask, render_template,  request
from markupsafe import escape

app = Flask(__name__)

moment = date.today().strftime("%d /%m/%Y")
H = datetime.now().strftime("%H:%M:%S")

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

@app.route("/page2")
def page2():
    return render_template("bjr2.html")

@app.route("/heure")
def heure():
    return render_template("heure.html", bonjour = "Hello World!",
    moment = moment, heure = H)

@app.route('/formulaire')
def formulaire():
    return render_template("formulaire.html")


@app.route('/reponse', methods=['POST'])
def reponse():    
    resultat = request.form
    nom = resultat['Nom']   
    prenom = resultat['Prénom']
    nomComplet = nom + " " + prenom
    return render_template("reponse.html" , message = nomComplet)


app.run(host="0.0.0.0", port=5000)
