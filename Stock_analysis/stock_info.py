import yahooquery as yq
import plotly
import pandas as pd

apple = yq.Ticker("AMD")
#print(apple.asset_profile)
print(apple.asset_profile)
apple_share_price_data = apple.history(period="max")
print(apple_share_price_data.head())
