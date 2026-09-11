n = 5
for i in range(1, n + 1):
    
    for j in range(1, i + 1):
        print(j, end=" ")
        
    spaces = (n - i) * 4 - 2 if i < n else 0
    print(" " * max(0, spaces), end="")
    
    start = i if i < n else n - 1
    for j in range(start, 0, -1):
        print(j, end=" " if j > 1 else "")
    print()