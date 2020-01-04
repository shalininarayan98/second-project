import numpy as np
from random import randint
from application import app
from flask import render_template


@app.route('/', methods=['GET', 'POST'])
def random_number():
    random_number=randint(1,10)

    return random_number
