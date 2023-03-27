from yahooquery import Ticker
import pandas as pd

symbols = 'AMD'

tickers = Ticker(symbols)

# Retrieve each company's profile information
data = pd.DataFrame(tickers)
data.to_excel('netflix.xlsx')