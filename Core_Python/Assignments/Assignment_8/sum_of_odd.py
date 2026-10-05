def odd(n):
    sum = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            sum = sum+ i
    return sum
    
n = int(input("Enter number:"))
res = odd(n)
print("Sum of odd numbers", res)