num = int(input("Enter a 3-digit number: "))

first_digit = num // 100       
second_digit = (num // 10) % 10 
third_digit = num % 10         

digit_sum = first_digit + second_digit + third_digit

print(f"Sum of digits of {num}: {digit_sum}")