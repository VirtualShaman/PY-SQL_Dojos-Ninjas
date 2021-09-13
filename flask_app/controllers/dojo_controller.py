from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def index():
    dojos = Dojo.getdojos()

    return render_template('index.html', dojos=dojos)

@app.route('/adddojo', methods = ["POST"])
def adddojo():
    data = {
        "dojo_name" : request.form["dojo_name"]
    }
    Dojo.adddojo(data)

    return redirect("/")

@app.route('/dojo/<int:id>')
def onedojo(id):
    data = {
        'id': id,
    }

    dojo = Dojo.onedojo(data)

    return render_template('ninjalist.html', dojo=dojo)