from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninjas():
    dojos = Dojo.getdojos()

    return render_template('addninjas.html', dojos=dojos)

@app.route('/newninjas', methods=['POST'])
def newninjas():
    data = {
        "dojo_id" : request.form['dojo_id'],
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age']
    }

    Ninja.newninja(data)

    return redirect(f"/dojo/{data['dojo_id']}")