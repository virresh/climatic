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
    


# @app.route('/<country>/<year>')
# def get_prediction(country, year):
#     # return str(random.randint(30, 50))+" degree celsius for "+country+" for the "+str(year)
#     country_data = original_data[country]
#     for yearc in country_data:
#         if(yearc==year):
#             return str(original_data[country][year])+" degree celsius for "+country+" for the "+str(year)
#     return str(random.randint(30, 50))+" degree celsius for "+country+" for the "+str(year)

port = int(os.getenv('VCAP_APP_PORT', 8080))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
