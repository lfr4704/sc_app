from flask import Flask, request
import openaq
import requests
import pandas as pd
import numpy as np
APP = Flask(__name__)
@APP.route('/')
def root():
    PARAMS = {
    'city': 'Los Angeles',
    'parameter':'pm25'
    }
    URL='https://api.openaq.org/v1/measurements'
    r = requests.get(url=URL, params=PARAMS)
    response = r.json()
    print(f"Meta:{response['meta']}")
    print(f"results:{len(response['results'])}")
    return response
