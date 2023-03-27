import yfinance

ticket = yfinance.Ticker('GME')

ticket_data = ticket.history(period='max')

print(ticket)

ticket_data.reset_index(inplace=True)

print(ticket_data.head())