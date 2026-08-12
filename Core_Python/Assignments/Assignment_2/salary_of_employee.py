basic = float(input("Enter Basic Salary: "))

# Calculate allowances based on percentage of basic salary
da = 0.10 * basic   # 10% Dearness Allowance
ta = 0.12 * basic   # 12% Travel Allowance
hra = 0.15 * basic  # 15% House Rent Allowance

# Calculate total salary
total_salary = basic + da + ta + hra

# Display detailed breakdown
print("\n--- Salary Breakdown ---")
print(f"Basic Salary: {basic}")
print(f"DA (10%):     {da}")
print(f"TA (12%):     {ta}")
print(f"HRA (15%):    {hra}")
print("------------------------")
print(f"Total Salary: ${total_salary}")