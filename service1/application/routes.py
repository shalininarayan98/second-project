from random import randint
from application import app
from flask import render_template
import requests


@app.route('/', methods=['GET', 'POST'])
def random_number():
    number=randint(1,3)

    return str(number)
