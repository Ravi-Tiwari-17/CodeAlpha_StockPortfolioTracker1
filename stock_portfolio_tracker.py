# CodeAlpha Task 2: Stock Portfolio Tracker

# Dictionary with stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130,
    "MSFT": 320
}

print("📊 Welcome to the Stock Portfolio Tracker!\n")

total_investment = 0
portfolio = {}

while True:
    stock = input("Enter stock symbol (AAPL, TSLA, GOOG, AMZN, MSFT) or 'done' to finish: ").upper()
    if stock == 'DONE':
        break
    elif stock in stock_prices:
        quantity = int(input(f"Enter quantity of {stock}: "))
        investment = stock_prices[stock] * quantity
        portfolio[stock] = investment
        total_investment += investment
    else:
        print("❌ Invalid stock symbol. Please try again.")

print("\n----- Investment Summary -----")
for stock, amount in portfolio.items():
    print(f"{stock}: ₹{amount}")

print(f"\n💰 Total Investment Value: ₹{total_investment}")

# Optional: Save result to a text file
with open("portfolio_summary.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("-----------------------\n")
    for stock, amount in portfolio.items():
        file.write(f"{stock}: ₹{amount}\n")
    file.write(f"\nTotal Investment Value: ₹{total_investment}\n")

print("\n✅ Portfolio saved to 'portfolio_summary.txt'")
