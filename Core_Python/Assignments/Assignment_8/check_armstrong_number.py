def count_digits(n):
    count = 0

    while n > 0:
        count = count + 1
        n = n // 10

    return count


def is_armstrong(n):
    original = n
    digits = count_digits(n)
    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit ** digits
        n = n // 10

    if total == original:
        return True
    else:
        return False


n = int(input("Enter a number: "))

if is_armstrong(n):
    print("Armstrong number")
else:
    print("Not an Armstrong number")