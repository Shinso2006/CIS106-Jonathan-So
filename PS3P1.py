ticker = input("Enter the stock ticker symbol: ")
shares = float(input("Enter number of shares: "))
cost_per_share = float(input("Enter cost per share: "))

amount_invested = shares * cost_per_share

print(f"Ticker: {ticker}")
print(f"Amount Invested: ${amount_invested:.2f}")
