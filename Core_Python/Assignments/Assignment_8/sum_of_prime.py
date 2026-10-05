def prime(n):
    if n <=1:
        return False

    for i in range(2, n):
        if n% i == 0:
            return False
    return True

def prime_sum(n):
    total = 0
    for i in range(1, n+1):
        if prime(i):
            total = total + i
    return total

n = int(input("Enter number:"))
print("Sum of Prime Numbers:", prime_sum(n))