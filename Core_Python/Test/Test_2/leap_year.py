y = int(input('Enter year:'))
if (y % 4 == 0 and y % 100 != 0):
    print(f'{y} is a leap year.')

else:
    print(f'{y} is not a leap year')