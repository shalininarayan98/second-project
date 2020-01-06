import requests

@app.route('/', methods=['GET', 'POST'])

def prediction():
    if random_letter=='A' and random_number==1:
        return 'A new job or role is on the horizon for 2020'
    elif random_letter=='A' and random_number==2:
        return 'Wave farewell to bad habits and enjoy a healthier bank balance as a result'
    elif random_letter=='A' and random_number==3:
        return 'expect a new/ exisiting partner in hold significance in 2020'
    elif random_letter=='A' and random_number==4:
        return 'travel, your world is your oyster'
    elif random_letter=='A' and random_number==5:
        return 'you might break your leg during summer'
    elif random_letter=='A' and random_number==6:
        return 'you might stub your toe'

    

response=requests.get("http://localhost:5000")
print(response.text)

requests.post("http://localhost:5000", json={random_letter}
