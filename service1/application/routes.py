import numpy as np
from random import randint
from application import app
from flask import render_template
import requests

@app.route('/', methods=['GET', 'POST'])
def random_number():
    random_number=randint(1,10)

    return random_number

response=requests.get("http://localhost:5000")
print(response.text)

requests.post("http://localhost:5000", json={random_number}
