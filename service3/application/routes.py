import requests
from flask import request
from application import app, db
import requests
from application.models import *
from sqlalchemy import *

@app.route('/', methods=['GET', 'POST'])
def prediction():


    random_number=requests.get('http://service1:5001').text
    random_letter=requests.get('http://service2:5002').text

    if random_letter=='A' and random_number=='1':
        return 'in a world full of fish you are going to be a shark'
    elif random_letter=='A' and random_number=='2':
        return 'wave farewell to bad habits and enjoy a healthier bank balance as a result'
    elif random_letter=='A' and random_number=='3':
        return 'expect significant progress in your love life'
    elif random_letter=='B' and random_number=='1':
        return 'travel, the world is your oyster'
    elif random_letter=='B' and random_number=='2':
        return 'expect a big promotion this year'
    elif random_letter=='B' and random_number=='3':
        return 'the pressure is high in all aspects of your life, be prepared for a rollarcoaster this year'
    elif random_letter=='C' and random_number=='1':
        return '2020 will be a fantasic year for you finacially'
    elif random_letter=='C' and random_number=='2':
        return 'your health will take a hit this year, take precautions in your lifestyle choices'
    else:
        return 'your loyalities towards people will need to be reassessed this year, do not be naive'

def post():
    if prediction.ok:
        return requests.get('http://service1:5001').text and requests.get('http://service2:5002').text
    else:
        return 'error'

'''


    if random_letter=='A' and random_number=='1':
        outcome1=Predictions.query(predictionID=1)
        return outcome1
    print(outcome1)


    
    

    elif random_letter=='A' and random_number=='2':
        outcome2 = Predictions.query(predictionID[2])
        return str(outcome2)
    elif random_letter=='A' and random_number=='3':
        outcome3 = Predictions.query(predictionID[3])
        return str(outcome3)
    elif random_letter=='B' and random_number=='1':
        outcome4 = Predictions.query(predictionID[4])
        return str(outcome4)
    elif random_letter=='B' and random_number=='2':
        outcome5 = Predictions.query(predictionID[5])
        return str(outcome5)
    elif random_letter=='B' and random_number=='3':
        outcome6 = Predictions.query(predictionID[6])
        return str(outcome6)
    elif random_letter=='C' and random_number=='1':
        outcome7 = Predictions.query(predictionID[7])
        return str(outcome7)
    elif random_letter=='C' and random_number=='2':
        outcome8 = Predictions.query(predictionID[8])
        return str(outcome8)
    else:
        outcome9 = Predictions.query(predictionID[9])
        return str(outcome9)

def post():
    if prediction.ok:
        return requests.get('http://service1:5001').text and requests.get('http://service2:5002').text
    else:
        return 'error'


    if random_letter=='A' and random_number=='1':
        return 'in a world full of fish you are going to be a shark'
    elif random_letter=='A' and random_number=='2':
        return 'wave farewell to bad habits and enjoy a healthier bank balance as a result'
    elif random_letter=='A' and random_number=='3':
        return 'expect significant progress in your love life'
    elif random_letter=='B' and random_number=='1':
        return 'travel, the world is your oyster'
    elif random_letter=='B' and random_number=='2':
        return 'expect a big promotion this year'
    elif random_letter=='B' and random_number=='3':
        return 'the pressure is high in all aspects of your life, be prepared for a rollarcoaster this year'
    elif random_letter=='C' and random_number=='1':
        return '2020 will be a fantasic year for you finacially'
    elif random_letter=='C' and random_number=='2':
        return 'your health will take a hit this year, take precautions in your lifestyle choices'
    else:
        return 'your loyalities towards people will need to be reassessed this year, do not be naive'

def post():
    if prediction.ok:
        return requests.get('http://service1:5001').text and requests.get('http://service2:5002').text
    else:
        return 'error'


@app.route('/', methods=['GET', 'POST'])
def prediction():


    random_number=requests.get('http://service1:5001').text
    random_letter=requests.get('http://service2:5002').text

    if random_letter=='A' and random_number=='1':
        outcome1 = prediction.query.filter_by(predictionID = 1)
        return outcome1
    elif random_letter=='A' and random_number=='2':
        outcome2 = prediction.query.filter_by(predictionID = 2)
        return outcome2
    elif random_letter=='A' and random_number=='3':
        outcome3 = prediction.query.filter_by(predictionID = 3)
        return outcome3
    elif random_letter=='B' and random_number=='1':
        outcome4 = prediction.query.filter_by(predictionID = 4)
        return outcome4
    elif random_letter=='B' and random_number=='2':
        outcome5 = prediction.query.filter_by(predictionID = 5)
        return outcome5
    elif random_letter=='B' and random_number=='3':
        outcome6 = prediction.query.filter_by(predictionID = 6)
        return outcome6
    elif random_letter=='C' and random_number=='1':
        outcome7 = prediction.query.filter_by(predictionID = 7)
        return outcome7
    elif random_letter=='C' and random_number=='2':
        outcome8 = prediction.query.filter_by(predictionID = 8)
        return outcome8
    else:
        outcome9 = prediction.query.filter_by(predictionID = 9)
        return outcome9

'''
