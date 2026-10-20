def max_profit(n):
    prices = list(range(n, 0,-1)) + list(range(n, n + 1))
    min_price, profit = prices[0], 0
    for p in prices[1:]:
        min_price = min(min_price, p)
        profit = max(profit, p - min_price)
    return profit

input("max_profit(n) finds best the best sisngle buy-sell in prices [1..n, n..1]  press enter")
print(" max_profit(4)=", max_profit(4))
print(" max_profit(5)=", max_profit(5))
n = int(input("Enter a number: "))
guess = input("What is max_profit(" + str(n) + ")? ")
input("track min price so far, sell when the gap meets its current best, press enter") 
print(" max_profit(" + str(n) + ") =", max_profit(n), " your guess:", guess)