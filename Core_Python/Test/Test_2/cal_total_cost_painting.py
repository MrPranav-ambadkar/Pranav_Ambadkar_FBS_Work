w = float(input('Enter width:'))
h = float(input('Enter height:'))
cost_per_sq_unit = float(input("Enter cost per unit:"))

single_wall_area = w * h
total_wall_area = single_wall_area * 4
total_cost = total_wall_area * cost_per_sq_unit

print(f'Total cost of Painting: {total_cost}')