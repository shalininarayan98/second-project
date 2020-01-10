from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import *
from application import app, db
import requests

@app.route('/', methods=['GET','POST'])
def service4():
    prediction=requests.post("http://service3:5003")

    if prediction.ok:
        random_number=requests.get('http://service1:5001').text
        random_letter=requests.get('http://service2:5002').text
        prediction=prediction.get('http://service3:5003').text
    
    return render_template('home.html', random_number=random_number, random_letter=random_letter, prediction=prediction)



'''

@app.route('/', methods=['GET','POST'])
def service4():
    prediction=""

    response=requests.post("http://service3:5003")

    prediction = response.text

    return prediction

    return render_template('home.html', title= 'prediction', response=request.txt, prediction=prediction)
    
    return ok



    app.logger.info("***************************************")
    app.logger.info(response)

    prediction = response.json()['p']

    return prediction

    return render_template('home.html', title= 'prediction', response=request.txt, prediction=prediction)
'''
