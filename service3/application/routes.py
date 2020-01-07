import requests
from flask import request
from application import app


@app.route('/', methods=['GET', 'POST'])

def prediction():

    if random_letter=='A' and random_number==1:
        return 'A new job or role is on the horizon for 2020'
    elif random_letter=='A' and random_number==2:
        return 'Wave farewell to bad habits and enjoy a healthier bank balance as a result'
    elif random_letter=='A' and random_number==3:
        return 'Expect significant progress in your current love life'
    elif random_letter=='B' and random_number==1:
        return 'Travel, the world is your oyster'
    elif random_letter=='B' and random_number==2:
        return 'You’re going to be offered chances to progress further than you currently believe is possible in your career'
    elif random_letter=='B' and random_number==3:
        return 'The pressure is high in all aspects of your life, be prepared for a rollarcoaster this year'
    elif random_letter=='C' and random_number==1:
        return '2020 will be a fantasic year for you finacially'
    elif random_letter=='C' and random_number==2:
        return 'Your health will take a hit this year, take precautions in your lifestyle choices'
    elif random_letter=='C' and random_number==3:
        return 'Your loyalities towards people will need to be reassessed this year, do not be naive'

