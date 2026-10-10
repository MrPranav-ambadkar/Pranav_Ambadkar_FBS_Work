def reverce_num(n, rev = 0):
    if n == 0:
        return rev

    digit = n % 10
    rev = rev * 10 + digit

    return reverce_num(n // 10, rev)

n = int(input("Enter a number: "))
res = reverce_num(n)
print("Reversed number is:", res)