numbers = [1, 3, 4, 1, 2, 3, 6, 7, 1, 2, 4]

freq = {}

for num in numbers:
    if num in freq:
        freq[num] = freq[num] + 1
    else:
        freq[num] = 1

print(freq)