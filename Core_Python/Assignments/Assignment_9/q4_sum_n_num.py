def son(n):
    if n == 0:
        return 0
    else:
        return n + son(n - 1)

n = int(input("Enter a number: "))
res = son(n)
print("Sum of n numbers is:", res)
