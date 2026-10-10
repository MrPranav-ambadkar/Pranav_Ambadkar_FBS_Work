def reverse_num(n, rev=0):
    if n == 0:
        return rev
    else:
        digit = n % 10
        rev = rev * 10 + digit
        return reverse_num(n // 10, rev)


n = int(input("Enter a number: "))

result = reverse_num(n)

print("Reverse =", result)