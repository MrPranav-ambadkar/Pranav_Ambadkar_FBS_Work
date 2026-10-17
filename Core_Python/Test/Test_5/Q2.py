n = int(input("Enter number of coins: "))

coins = list(map(int, input("Enter coin numbers: ").split()))

freq = {}

for coin in coins:
    if coin in freq:
        freq[coin] += 1
    else:
        freq[coin] = 1

for coin in freq:
    if freq[coin] % 2 != 0:
        print("Missing coin:", coin)
        break
