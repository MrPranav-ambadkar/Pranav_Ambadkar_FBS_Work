n = int(input("Enter number of students: "))

total_percentage = 0

for i in range(n):
    print(f"Enter marks for Student {i + 1}")

    total_marks = 0

    for j in range(5):
        marks = float(input(f"Enter marks subject {j + 1}: "))
        total_marks += marks

    percentage = total_marks / 5
    print(f"Percentage: {percentage}")

    total_percentage += percentage

average = total_percentage / n

print(f"Average percentage of all students: {average}")