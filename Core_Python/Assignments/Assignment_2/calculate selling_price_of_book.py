cost_price = float(input("Enter Cost Price of the book: "))
discount_percent = float(input("Enter Discount Percentage (%): "))

discount_amount = cost_price * (discount_percent / 100)
selling_price = cost_price - discount_amount

print(f"\nDiscount Amount: {discount_amount}")
print(f"Selling Price: {selling_price}")