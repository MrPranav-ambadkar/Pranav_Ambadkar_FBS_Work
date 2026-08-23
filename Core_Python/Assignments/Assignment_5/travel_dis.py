passengers = int(input("Enter number of passengers: "))
ticket_cost = float(input("Enter ticket cost: "))

total_amount = 0

for i in range(passengers):
    age = int(input("Enter age of passenger: "))

    if age < 12:
        amount = ticket_cost - (ticket_cost * 30 / 100)
    elif age > 59:
        amount = ticket_cost - (ticket_cost * 50 / 100)
    else:
        amount = ticket_cost

    total_amount += amount

print("Total ticket amount:", total_amount)