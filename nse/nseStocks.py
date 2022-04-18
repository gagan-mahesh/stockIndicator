#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import numpy as np
from datetime import datetime
import plotly.graph_objects as go
from datetime import date
from nsepy import get_history
import pandas as pd
import matplotlib.pyplot as plt

from pandas.plotting import scatter_matrix


def getDateDataframe(df):
    arr = []  # temporary array to hold dates
    for i in range(len(df)):
        arr.append(df.iloc[i].name)
    df['Date'] = arr
    return df


def getPortfolioData(p, startYear, startMonth, startDay, endYear, endMonth, endDay):
    data = get_history(symbol=p, start=date(
        startYear, startMonth, startDay), end=date(endYear, endMonth, endDay))
    data = pd.DataFrame(data[['Close', 'Open', 'High', 'Low']])
    data = getDateDataframe(data)
    df = {}
    df['Date'] = data['Date'].to_list()
    df['Close'] = data['Close'].to_list()
    df['Open'] = data['Open'].to_list()
    df['High'] = data['High'].to_list()
    df['Low'] = data['Low'].to_list()
    return df


def get_rsi(close, lookback):
    change = close.diff()
    gain = [0]
    loss = [0]

    n = len(close)
    for i in range(1, n):
        gain.append(max(change[i], 0))
        loss.append(abs(min(change[i], 0)))

    # calculate exp moving avg
    gain = pd.Series(gain)
    gain_mean = gain.ewm(span=lookback, min_periods=lookback-1).mean()
    loss = pd.Series(loss)
    loss_mean = loss.ewm(com=lookback, min_periods=lookback-1).mean()

    rs = [np.nan]
    rsi = [0]

    for i in range(1, n):
        if loss_mean[i] == 0:
            rsi[i] = float('inf')
            break
        rs.append(gain_mean[i] / loss_mean[i])
        rsi.append(100-100/(1+rs[i]))
    return rsi
