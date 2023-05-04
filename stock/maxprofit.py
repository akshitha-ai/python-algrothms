def max_profit(prices):
min_price = float('inf')
max_profit = 0
for price in prices:{}
    if price < min_price:
        min_price = price
    else:
        potential_profit = price - min_price
        if potential_profit > max_profit:
            max_profit = potential_profit
            return max_profit
    
prices=[2,4,6,1,9]
max_profit = max_profit(prices)
print(f"Max Profit: {max_profit}")


