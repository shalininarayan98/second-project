from random import randint
from application import app
from flask import render_template
import requests


@app.route('/', methods=['POST'])
def random_number():
    number=randint(1,3)

    return number
'''
requests.post("http://localhost:5000", json={random_number})

if __name__ == '__main__':
    app.run (host='0.0.0.0', port=5001)
'''
