import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
import yfinance as yf
import datetime as dt


# To-DO : 
# [feat] Add UI with streamlit and host
# [feat] Add serach option
# [feat] Add more options and add better labels on plot


ticker = 'GOOG'

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
avgerate_loss = abs(negative.rolling(window=days).mean())

# calc relative strength 
relative_strength = avgerate_gain / avgerate_loss
RSI = 100.0 - (100.0 / (1.0 + relative_strength))

combined = pd.DataFrame()
combined['Adj Close'] = data['Adj Close']
combined['RSI'] = RSI


plt.figure(figsize=(12,8))

# Adj close price chart
ax1 = plt.subplot(211)
ax1.plot(combined.index, combined['Adj Close'], color='lightblue')

ax1.set_title("Adjusted Close Price", color='white')

ax1.grid(True, color='#f7f7f7')

ax1.set_axisbelow(True)
ax1.set_facecolor('black')
ax1.figure.set_facecolor('#121212')

ax1.tick_params(axis='x', color='white')
ax1.tick_params(axis='y', color='white')

# RSI chart
ax2 = plt.subplot(212, sharex=ax1)

ax2.plot(combined.index, combined['RSI'], color='lightblue')

ax2.axhline(0, linestyle='--', alpha=0.5, color='lightgray')
ax2.axhline(10, linestyle='--', alpha=0.5, color='#ff0000')
ax2.axhline(20, linestyle='--', alpha=0.5, color='#ffaa00')
ax2.axhline(30, linestyle='--', alpha=0.5, color='#cccccc')
ax2.axhline(70, linestyle='--', alpha=0.5, color='lightgray')
ax2.axhline(80, linestyle='--', alpha=0.5, color='#00ff00')
ax2.axhline(90, linestyle='--', alpha=0.5, color='#ffaa00')
ax2.axhline(100, linestyle='--', alpha=0.5, color='#ff0000')


ax2.set_title('RSI value', color='white')
ax2.grid(False)

ax2.set_axisbelow(True)
ax2.set_facecolor('black')

ax2.tick_params(axis='x', color='white')
ax2.tick_params(axis='y', color='white')

# plt.show()
plt.savefig('goog_rsi_chart.png')  # Save the figure
plt.close() 


