"""
A simple chatting application made using flask backend and uses AJAX Polling
"""

import datetime
import time
import os
from flask import Flask, render_template, request, session, escape
import random
import csv
import urllib
import pickle


pickle_in = open("data","rb")
original_data = pickle.load(pickle_in)
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'WHY_SO_MUCH_TORTURE?')


@app.route('/')
def home_page():
    p = [['Country', 'Value']]
    country_list_link = 'https://gist.githubusercontent.com/mbostock/4090846/raw/07e73f3c2d21558489604a0bc434b3a5cf41a867/world-country-names.tsv'
    f = urllib.request.urlopen(country_list_link)
    countries = [[row.split('\t')[1], random.randint(30, 50)] for row in f.read().decode('UTF-8').split('\n') if row]
    # print(countries)
    countries.pop(0)
    p.extend(countries)
    years = [2016, 2017, 2018]
    return render_template('evs.html', years=years, countries=p)

@app.route('/<country>/<year>')
def get_prediction(country, year):
    # return str(random.randint(30, 50))+" degree celsius for "+country+" for the "+str(year)
    country_data = original_data[country]
    for yearc in country_data:
        if(yearc==year):
            return str(original_data[country][year])+" degree celsius for "+country+" for the "+str(year)
    return str(random.randint(30, 50))+" degree celsius for "+country+" for the "+str(year)

port = int(os.getenv('VCAP_APP_PORT', 8080))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
