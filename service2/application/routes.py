import random
import string
import requests
from application import app


@app.route('/', methods=['GET', 'POST'])

def random_letter():
    upper_alphabet = string.ascii_uppercase
    letter = random.choice(upper_alphabet[0:3])
    
    return letter

#response=requests.get("http://localhost:5000")
#print(response.text)

#requests.post("http://localhost:5000", json={random_letter})
