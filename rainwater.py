def rainwater(n):
    bars = [0, n, 0, n, 0]
    return min(max(bars[:3]), max(bars[2:])) - bars[2]

input("rainwater(n) traps water between 2 bars of height n. press enter ")
print("rainwater(4) =", rainwater(4))
print("rainwater(5) =", rainwater(5))

n = int(input("Enter a number: "))
guess = input("What is rainwater(" + str(n) + ")? ")
input("water = n(left tallest, right tallest) - bar height at gap. press enter ")
print(" rainwater(" + str(n) + ") =", rainwater(n), "your guess:", guess)