l = 50
b = 40
r = 20
layers = 5
cost_per_meter = 35
pi = 22 / 7

arc_length = pi * r
perimeter = (2 * l) + b + arc_length
total_wire_length = perimeter * layers
total_cost = total_wire_length * cost_per_meter

print(f'Field perimeter: {perimeter} meters')
print(f'Total wire required: {total_wire_length} meter')
print(f'Total cost of fencing: Rs. {total_cost}')