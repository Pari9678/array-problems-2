def total_profit(n):
    prices = [1, n, 1, n, 1]
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit

input("total_prices(n) sums every upswing in prices [1, n, 1, n, 1], press enter ")
print("total_profit(4) =", total_profit(4))
print("total_profit(5) =", total_profit(5))

n = int(input("Enter a number: "))
guess = input("what is total_profit(" + str(n) + ")? ")
input("add every positive step, 2 peak each contribute n - 1. press enter ")
print("total_profit(" + str(n) + ") =", total_profit(n), "your guess:", guess)