"""
A simple chatting application made using flask backend and uses AJAX Polling
"""

import datetime
import time
import os
from flask import Flask, render_template, request, session, escape
import random

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'WHY_SO_MUCH_TORTURE?')


@app.route('/')
def home_page():
    return render_template('home.html', greeting='Hello From Group 11. Our EVS Project on climate change')

@app.route('/<country>/<year>')
def get_prediction(country, year):
    return str(random.randint(30, 50))+" degree celsius for "+country+" for the "+str(year)

port = int(os.getenv('VCAP_APP_PORT', 8080))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
