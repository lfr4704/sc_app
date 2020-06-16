from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import openaq
import requests
import pandas as pd
import numpy as np
APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB = SQLAlchemy(APP)
@APP.route('/')
def root():
    PARAMS = {
    'city': 'Los Angeles',
    'parameter':'pm25'
    }
    URL='https://api.openaq.org/v1/measurements'
    r = requests.get(url=URL, params=PARAMS)
    response = r.json()
    my_list = []
    for x in response['results']:
        print(response['results'][1]['date']['utc'])
    print(f"UTC: {response['results'][1]['date']['utc']}")
    print(f"Meta:{response['meta']}")
    print(f"results:{len(response['results'])}")
    return response
class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String(25))
    value = DB.Column(DB.Float, nullable=False)
    def __repr__(self):
        return 'TODO - write a nice representation of Records'
@APP.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    DB.drop_all()
    DB.create_all()
    # TODO Get data from OpenAQ, make Record objects with it, and add to db
    DB.session.commit()
    return 'Data refreshed!'
