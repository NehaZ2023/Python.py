import pandas as pd
import yfinance as yf

# Specify company tickers and a period
tickers = ["AAPL", "GOOG", "MSFT", "AMZN"]
period = "1y"  # Adjust as needed

# Retrieve current stock prices
current_prices = yf.download(tickers, period=period)["Adj Close"].iloc[-1]

# Calculate percentage change over the period
pct_change = (current_prices - current_prices.shift(1)) / current_prices.shift(1) * 100

# Display results
print("Current Stock Prices:")
print(current_prices)
print("\nPercentage Change:")
print(pct_change)

# Identify best performing stock
best_performer = pct_change.idxmax()
print("\nBest Performing Stock:", best_performer)

# Retrieve historical stock prices
historical_prices = yf.download(tickers, period=period)

# Analyze trends and patterns (optional)
# ... (Perform analysis using pandas methods as needed)