import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
import yfinance as yf
import datetime as dt


ticker = 'META'

start = dt.datetime(2023, 1, 1)
end = dt.datetime.now()

data = yf.download(ticker,start=start, end=end)

print(data)