import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Input portfolio
stocks = input("Enter stock symbols separated by commas (e.g., TCS.NS, INFY.NS): ").split(",")
shares = input("Enter number of shares for each stock separated by commas: ").split(",")

shares = [int(s) for s in shares]

# Fetch stock data
data = yf.download(stocks, period="6mo")['Adj Close']

# Calculate portfolio value
portfolio = data * shares
portfolio['Total'] = portfolio.sum(axis=1)

# Display summary
print("\nPortfolio Value Summary:")
print(portfolio['Total'].describe())

# Daily returns
daily_returns = portfolio['Total'].pct_change().dropna()
print("\nDaily Returns Summary:")
print(daily_returns.describe())

# Plot portfolio performance
plt.figure(figsize=(10,6))
plt.plot(portfolio['Total'], label='Portfolio Value')
plt.title("Portfolio Performance")
plt.xlabel("Date")
plt.ylabel("Value (INR)")
plt.legend()
plt.show()
