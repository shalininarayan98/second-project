from random import randint
from application import app
from flask import render_template
import requests


@app.route('/', methods=['GET', 'POST'])
def random_number():
    number=randint(4,6)

    return str(number)
