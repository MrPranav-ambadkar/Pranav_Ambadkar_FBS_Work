n  = int(input("Enter a number of Employees:"))
total_sal_all_emp = 0

for i in range(1, n+1):
    basic = float(input(f'Enter the basic Salary for Employee {i}:'))

    if basic < 20000:
        da_per, ta_per, hra_per = 10, 12, 15

    else:
        da_per, ta_per, hra_per = 15, 18, 20

    da = basic + (da_per / 100)
    ta = basic + (ta_per / 100)
    hra = basic + (hra_per / 100)

    total_sal_each = basic + da + ta + hra
    total_sal_all_emp += total_sal_each
    print("Total Salary of Employee", i, total_sal_each)

    total_sal_all_emp += total_sal_each

print(f'Grand Total Salary of all {n} employees: {total_sal_all_emp:.2f}')