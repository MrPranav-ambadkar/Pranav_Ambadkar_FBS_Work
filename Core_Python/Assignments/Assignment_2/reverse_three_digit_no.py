num = int(input("Enter a 3-digit number: "))

# Extract digits
first_digit = num // 100        # e.g., 456 // 100 = 4
second_digit = (num // 10) % 10 # e.g., (456 // 10) % 10 = 5
third_digit = num % 10          # e.g., 456 % 10 = 6

# Rebuild in reverse order
reversed_num = (third_digit * 100) + (second_digit * 10) + first_digit

print(f"Reversed number: {reversed_num}")