# a. Sum of 1 + 2 + 3 + ... + n

def sum_numbers(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total


# b. Sum of 1! + 2! + 3! + ... + n!

def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    return fact


def sum_factorials(n):
    total = 0

    for i in range(1, n + 1):
        total = total + factorial(i)

    return total


# c. Sum of 1^1 + 2^2 + 3^3 + ... + n^n

def sum_powers(n):
    total = 0

    for i in range(1, n + 1):
        total = total + (i ** i)

    return total


# Main program

n = int(input("Enter n: "))

print("Sum of 1 + 2 + 3 + ... + n =", sum_numbers(n))

print("Sum of 1! + 2! + 3! + ... + n! =", sum_factorials(n))

print("Sum of 1^1 + 2^2 + 3^3 + ... + n^n =", sum_powers(n))