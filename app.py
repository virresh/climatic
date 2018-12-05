"""
A simple chatting application made using flask backend and uses AJAX Polling
"""

import datetime
import time
import os
from flask import Flask, render_template, request, session, escape, abort, Response
import random
import csv
import urllib
import pickle
import json

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'WHY_SO_MUCH_TORTURE?')


@app.route('/')
def home_page():
    return render_template('home.html', greeting=2050)

@app.route('/show/<year>')
def get_year(year):
    return render_template('home.html', greeting=year)

@app.route('/<year>')
def get_pred(year):
    csv = "location,temp\n"
    try:
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT, "static/data_json", "yearwise_CSV_{}.json".format(year))) as f:
            data = json.load(f)
        for i in data:
            csv += str(i['country'])+","+str(i['temp'])+"\n"
        return Response(csv, mimetype='text/csv')
        # print(csv)
    except Exception as e:
        print(e)
        # abort(404)
        print(year)
        return "location,temp\nIndia,37.7\n"

port = int(os.getenv('VCAP_APP_PORT', 8080))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
