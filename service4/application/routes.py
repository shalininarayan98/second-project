from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import *
from application import app, db
import requests

@app.route('/', methods=['GET','POST'])
def service4():
    prediction=""

    response=requests.post("http://service3:5003")
    app.logger.info("***************************************")
    app.logger.info(response)

    prediction = response.json()['p']

    return prediction

#    return render_template('home.html', title= 'prediction', response=request.txt, prediction=prediction)
