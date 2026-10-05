def reverce(n):
    reverce = 0
    while n > 0:
        digit = n % 10
        reverce = reverce * 10 + digit
        n = n // 10
    return reverce

n = int(input("Enter a number:"))
rev = reverce(n)
print("Reverce number", rev)
