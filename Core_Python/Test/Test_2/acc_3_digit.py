num = int(input('Enter 3 digit number:'))
first_digit = num //100
second_digit = (num // 10) % 10
third_digit = num %10

if first_digit == 2* second_digit and first_digit == third_digit / 2:
    print('Yes, you have done it')

else:
    print('Please try next time')