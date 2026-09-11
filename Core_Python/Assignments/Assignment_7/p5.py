n = 5

for i in range(1, n + 1):

    print("  " * (n - i), end="")

    if i == 1:
        print(1)

    elif i == n:
        # Last row: print 1 to n
        for j in range(1, n + 1):
            print(j, end="   ")
        print()

    else:
        print(1, end=" ")

        print("  " * (2 * i - 3), end="")

        print(i)