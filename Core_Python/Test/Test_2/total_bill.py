total_price = 0 

for i in range(1, 6):
    price = float(input(f'Enter the price of product {i}: '))
    total_price += price

gst_amount = total_price * 0.18
final_bill = total_price + gst_amount

print(f'Subtotal: {total_price}')
print(f' GST (18%): {gst_amount}')
print(f' Total Bill: {final_bill}')