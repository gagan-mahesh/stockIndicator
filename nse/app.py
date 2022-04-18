from flask import Flask
from nseStocks import *
import numpy as np
import pandas as pd

app = Flask(__name__)


@app.route('/')
def home():
    return 'Home page'

# localhost:4000/setPortfolio/tcs/start/3/3/2002/end/3/3/2022


@app.route('/setPortfolio/<portfolio>/start/<int:startDay>/<int:startMonth>/<int:startYear>/end/<int:endDay>/<int:endMonth>/<int:endYear>')
def setPortfolio(portfolio, startDay, startMonth, startYear, endDay, endMonth, endYear):
    res = getPortfolioData(portfolio, startYear, startMonth,
                           startDay, endYear, endMonth, endDay)
    return res, 200


app.run(debug=True, port=4000)
