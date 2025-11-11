# Q1:
# 3 ()
# 6700

# Q2:
# "0x9F1aB3c" + ... --> "0x9F1aB3c..."

# Q3:
holdings = {"BTC": 0.5, "ETH": 8.2, "SOL": 50}
price = {"BTC": 62400, "ETH": 2480, "SOL": 142}
def portfolio_value(holdings, prices):
    total = 0
    for stocks, amount in holdings.items():
        total += amount * prices[stocks]
    return round(total, 2)
print(portfolio_value(holdings, price))