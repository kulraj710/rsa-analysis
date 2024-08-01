import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
import yfinance as yf
import datetime as dt


ticker = 'META'

start = dt.datetime(2023, 1, 1)
end = dt.datetime.now()

data = yf.download(ticker,start=start, end=end)

delta = data['Adj Close'].diff(1)
delta.dropna(inplace=True)

positive = delta.copy()
negative = delta.copy()

# scrap negavite values
positive[ positive < 0] = 0

# scrap positive values
negative[ negative > 0] = 0

days = 14

avgerate_gain = positive.rolling(window=days).mean()
avgerate_loss = negative.rolling(windows=days).mean()

# calc relative strength 
relative_strength = avgerate_gain / avgerate_loss
RSI = 100.0 - (100.0 / (1.0 + relative_strength))

combined = pd.DataFrame()
combined['Adj Close'] = data['Adj Close']
combined['RSI'] = RSI


