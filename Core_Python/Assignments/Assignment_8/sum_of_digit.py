def sum_digits(n):
    total = 0
    while n > 0:
        digit = n %10
        total = total + digit
        n = n//10
    return total

n = int(input("Enter a number:"))
res = sum_digits(n)
print("Sum of digits:", res)