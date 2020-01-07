import random
import string
import requests

@app.route('/', methods=['GET', 'POST'])

def random_letter():
    upper_alphabet = string.ascii_uppercase
    random_letter = random.choice(upper_alphabet[0:3])
    return random_letter

response=requests.get("http://localhost:5000")
print(response.text)

requests.post("http://localhost:5000", json={random_letter}
