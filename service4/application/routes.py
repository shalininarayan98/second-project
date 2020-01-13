from flask import render_template, redirect, url_for, request
#from application import app, db
#from application.models import *
from application import app
import requests

@app.route('/', methods=['GET','POST'])
def service4():

    response=requests.post('http://service3:5003').text
    response=requests.post('http://service2:5002').text
    response=requests.post('http://service1:5001').text
#    response1=requests.post('http://service1:5001').text
#    response2=requests.post('http://service2:5002').text
    return response

'''
@app.route('/', methods=['GET','POST'])
def service4():

#    random_number=requests.get('http://service1:5001').text
#    random_letter=requests.get('http://service2:5002').text
    response=requests.post('http://service3:5003').text

    ## response=prediction.post('http://service3:5003').text
    
    ## return render_template('home.html', random_number=random_number, random_letter=random_letter, prediction=response)
    return response

@app.route('/', methods=['GET','POST'])
def service4():
#    prediction=requests.post("http://service3:5003")
    prediction=""

#    if prediction.ok:
#        random_number=requests.get('http://service1:5001').text
#        random_letter=requests.get('http://service2:5002').text
        response=prediction.post('http://service3:5003').text
    
        return render_template('home.html', random_number=random_number, random_letter=random_letter, prediction=requests)

    else:

        return 'error' 




@app.route('/', methods=['GET','POST'])
def service4():
    prediction=requests.post("http://service3:5003")

    random_number=requests.post('http://service1:5001').text
    random_letter=requests.post('http://service2:5002').text
    prediction=prediction.get('http://service3:5003').text
    if prediction.status_code==200:
        prediction=prediction.text

        
    return render_template('home.html', random_number=random_number, random_letter=random_letter, prediction=prediction)




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
