def minCoins(coins, amount, cnt):
    if (amount == 0):
        return cnt

    for i in range(0, len(coins)):
        if (coins[i] <= amount):
            return minCoins(coins, amount - coins[i], cnt + 1)
  
print("Enter amount of cents: ")
centsAmount = int(input())
coins = [200, 100, 25, 10, 5, 1]
print("Minimum coins amount: " + str(minCoins(coins, centsAmount, 0)))