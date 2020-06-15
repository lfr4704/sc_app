from flask import Flask, requests
import openaq
APP = Flask(__name__)
@APP.route('v1/measurements', methods=['GET', 'POST'])
def root():
    print(status)
    return 'TODO - part 2 and beyond!'
