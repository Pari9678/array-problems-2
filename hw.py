prices = [100, 180, 260, 310, 40, 535, 695]

profit = 0
for i in range(1, len(prices)):
    if prices[i] > prices[i - 1]:
        profit += prices[i] - prices[i - 1]

total_profit = profit

heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
left_tallest = [0] * len(heights)
left_tallest[0] = heights[0]
for i in range(1, len(heights)):
    left_tallest[i] = max(left_tallest[i - 1], heights[i])

right_tallest = [0] * len(heights)
right_tallest[-1] = heights[-1]
for i in range(len(heights) - 2, -1, -1):
    right_tallest[i] = max(right_tallest[i + 1], heights[i])

rainwater = 0
for i in range(len(heights)):
    rainwater += min(left_tallest[i], right_tallest[i]) - heights[i]

print("Stock Prices:", prices)
print("Total Profit:", total_profit)
print("Left Tallest:", left_tallest)
print("Right Tallest:", right_tallest)
print("Total Rainwater Trapped:", rainwater)