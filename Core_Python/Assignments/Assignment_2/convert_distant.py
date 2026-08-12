feet = float(input("Enter feet: "))
inches = float(input("Enter inches: "))

# Convert everything to total inches first
total_inches = (feet * 12) + inches

# Convert total inches to meters
meters = total_inches * 0.0254

# Convert meters to centimeters
centimeters = meters * 100

# Print results 
print(f"\nTotal distance:")
print(f"{meters} meters")
print(f"{centimeters} centimeters")