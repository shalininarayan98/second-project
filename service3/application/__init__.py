'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = ('mysql+pymysql://' + getenv('MY_SQL_USER') + ':' + getenv('MY_SQL_PASSWORD') + '@' + getenv('MY_SQL_URL') + '/' + getenv('MY_SQL_DB'))


app.config['SECRET_KEY'] = getenv('SECRET_KEY')


db = SQLAlchemy(app)



from application import routes
'''
import os
import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

user = os.getenv('MY_SQL_USER')
password = os.getenv('MY_SQL_PASSWORD')
url = os.getenv('MY_SQL_URL')
db = os.getenv('MY_SQL_DB')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{0}:{1}@{2}/{3}'.format(user, password, url, db)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] = 'SECRET_KEY'

db=SQLAlchemy(app)

from application import routes
