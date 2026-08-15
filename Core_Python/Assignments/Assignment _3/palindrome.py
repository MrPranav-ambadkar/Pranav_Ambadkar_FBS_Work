num = int(input("Enter a 3-digit number: "))

# Ensure it's a 3-digit number
if 100 <= abs(num) <= 999:
    first_digit = num // 100
    last_digit = num % 10

    if first_digit == last_digit:
        print(f"{num} is a Palindrome.")
    else:
        print(f"{num} is NOT a Palindrome.")
else:
    print("Please enter a valid 3-digit number.")