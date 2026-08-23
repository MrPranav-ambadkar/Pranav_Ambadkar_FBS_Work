print("1. 1! + 2! + 3! + ... + n!")
print("2. N + N^2 + N^3 + ... + N^N")
print("3. 1 + 2 + 4 + 8 + ...")
print("4. a + a^2/2 + a^3/3 + ... + a^10/10")
print("5. x - x^2/3 + x^3/5 - x^4/7 + ...")

choice = int(input("Enter your choice: "))

if choice == 1:
    n = int(input("Enter n: "))

    fact = 1
    total = 0

    for i in range(1, n + 1):
        fact = fact * i
        total = total + fact

    print("Sum =", total)


elif choice == 2:
    n = int(input("Enter N: "))

    total = 0

    for i in range(1, n + 1):
        total = total + n ** i

    print("Sum =", total)


elif choice == 3:
    n = int(input("Enter number of terms: "))

    term = 1
    total = 0

    for i in range(1, n + 1):
        total = total + term
        term = term * 2

    print("Sum =", total)


elif choice == 4:
    a = int(input("Enter a: "))

    total = 0

    for i in range(1, 11):
        total = total + (a ** i) / i

    print("Sum =", total)


elif choice == 5:
    x = int(input("Enter x: "))
    n = int(input("Enter number of terms: "))

    total = 0
    sign = 1

    for i in range(1, n + 1):
        term = (x ** i) / (2 * i - 1)
        total = total + sign * term
        sign = sign * -1

    print("Sum =", total)


else:
    print("Invalid choice")