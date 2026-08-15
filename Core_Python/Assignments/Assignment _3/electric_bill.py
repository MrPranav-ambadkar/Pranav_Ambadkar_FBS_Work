# Input total electricity units consumed
units = float(input("Enter total units consumed: "))

# Calculate bill amount based on unit slabs
if units <= 50:
    amount = units * 0.50
elif units <= 150:
    amount = (50 * 0.50) + ((units - 50) * 0.75)
elif units <= 250:
    amount = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)
else:
    amount = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 250) * 1.50)

# Calculate 20% surcharge
surcharge = amount * 0.20

# Calculate total bill
total_bill = amount + surcharge

# Display detailed breakdown
print("\n--- Electricity Bill ---")
print(f"Base Charges : Rs. {amount}")
print(f"Surcharge (20%): Rs. {surcharge}")
print(f"Total Amount  : Rs. {total_bill}")