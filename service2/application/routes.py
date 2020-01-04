import random
import string

@app.route('/', methods=['GET', 'POST'])
def random_letter():
    string.ascii_letters
    random.choice(string.ascii_letters[0:4])

    return random_letter
