from flask import render_template
from application import app


@app.route('/service4', methods=['Get','Post'])
def service4():
    response=requests.get("http://service1:5000")
    response1=requests.get("http://service2:5001")
    return render_template('.html', title= 'Response', response=request.txt, response1=requests.txt)i
