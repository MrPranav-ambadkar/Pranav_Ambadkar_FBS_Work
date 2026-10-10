def power(num, n):
    if n == 0:
        return 1
    return num * power (num, n - 1)

def armstrong(num, digits):
    if num == 0:
        return 0
    digit = num % 10
    return power(digit, digits) + armstrong(num // 10, digits)

n = int(input("Enter a number: "))
digits = len(str(n))
digits = armstrong(n, digits)

if digits == n:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")

