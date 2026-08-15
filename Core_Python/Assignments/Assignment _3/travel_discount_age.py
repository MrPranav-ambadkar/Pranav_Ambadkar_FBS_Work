no = int(input("Enter the number of tickets you want to buy: "))
totalAmount = 0
i = 1

while i <= no:
    age = int(input(f"Enter age of person {i}: "))
    tkp = float(input(f"Enter ticket price for person {i}: "))
    
    if age < 12:
        disco = tkp * 0.30
        print(f"Person {i} gets a 30% discount of Rs {disco:.2f}")
        totalAmount += (tkp - disco)
    elif age > 59:
        disco = tkp * 0.50
        print(f"Person {i} gets a 50% discount of Rs {disco:.2f}")
        totalAmount += (tkp - disco)
    else:
        print(f"Person {i} does not get any discount.")
        totalAmount += tkp
        
    i += 1

print(f"\nTotal Amount to pay for all tickets: Rs {totalAmount:.2f}")
