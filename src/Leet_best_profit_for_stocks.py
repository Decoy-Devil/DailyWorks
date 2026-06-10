


prices = [10, 1, 5, 6, 7, 1]

min_price = prices[0]   # best buy price seen so far (from past)
best_profit = 0         # best profit seen so far

print(min_price, best_profit)

for price in prices[1:]:
    profit_if_sell_today = price - min_price

    if profit_if_sell_today > best_profit:
        best_profit = profit_if_sell_today

    if price < min_price:
        min_price = price

print("min_price =", min_price)
print("best_profit =", best_profit)

# for price in prices [1:]:
#     print("today's price", price)
#     if best profit < (price - min price ) # 1 vs 5  = 5 - 1 = 4
#     then update best profit = price - min price
#     if price < min prince
#     then update min price to current price

