import pandas as pd
import matplotlib.pyplot as plt
from yahooquery import Ticker

tickers = Ticker('aapl', asynchronous=True)
df = tickers.history(period='max')
df["adjclose"].plot()
plt.xticks(rotation=90)
plt.show()