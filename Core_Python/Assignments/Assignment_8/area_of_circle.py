def Circle(radius):
    area = 3.14 * radius * radius
    return area

radius = float(input("Enter the radius of the circle: "))
res = Circle(radius)
print("Area of Circle", res)