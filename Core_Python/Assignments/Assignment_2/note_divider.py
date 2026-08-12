amount = int(input("Enter amount: "))

temp_amount = amount

n2000 = temp_amount // 2000
temp_amount %= 2000

n500 = temp_amount // 500
temp_amount %= 500

n200 = temp_amount // 200
temp_amount %= 200

n100 = temp_amount // 100
temp_amount %= 100

n50 = temp_amount // 50
temp_amount %= 50

n20 = temp_amount // 20
temp_amount %= 20

n10 = temp_amount // 10
temp_amount %= 10

n5 = temp_amount // 5
temp_amount %= 5

n2 = temp_amount // 2
temp_amount %= 2

n1 = temp_amount // 1
temp_amount %= 1

total_notes = n2000 + n500 + n200 + n100 + n50 + n20 + n10 + n5 + n2 + n1

print("\n--- Breakdown of Notes ---")
print(f"₹2000 notes : {n2000}")
print(f"₹500 notes  : {n500}")
print(f"₹200 notes  : {n200}")
print(f"₹100 notes  : {n100}")
print(f"₹50 notes   : {n50}")
print(f"₹20 notes   : {n20}")
print(f"₹10 notes   : {n10}")
print(f"₹5 notes    : {n5}")
print(f"₹2 notes    : {n2}")
print(f"₹1 notes    : {n1}")
print("--------------------------")
print(f"Total minimum notes needed: {total_notes}")