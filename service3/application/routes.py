import requests
from flask import request
from application import app
import requests

@app.route('/', methods=['GET', 'POST'])


def prediction():
    random_number = requests.post('http://service1:5001').text
    random_letter = requests.post('http://service2:5002').text


    if random_letter=='A' and random_number=='1':
        return {"p":'In a world full of fish you are going to be a shark'}
    elif random_letter=='A' and random_number=='2':
        return {"p"'Wave farewell to bad habits and enjoy a healthier bank balance as a result'}
    elif random_letter=='A' and random_number=='3':
        return {"p":'Expect significant progress in your love life'}
    elif random_letter=='B' and random_number=='1':
        return {"p":'Travel, the world is your oyster'}
    elif random_letter=='B' and random_number=='2':
        return {"p":'Expect a big promotion this year'}
    elif random_letter=='B' and random_number=='3':
        return {"p":'The pressure is high in all aspects of your life, be prepared for a rollarcoaster this year'}
    elif random_letter=='C' and random_number=='1':
        return {"p":'2020 will be a fantasic year for you finacially'}
    elif random_letter=='C' and random_number=='2':
        return {"p":'Your health will take a hit this year, take precautions in your lifestyle choices'}
    else:
        return {"p":'Your loyalities towards people will need to be reassessed this year, do not be naive'}
