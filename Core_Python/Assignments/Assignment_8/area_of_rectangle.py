def Rectangle(length, breadth):
    area = length * breadth
    return area
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
res = Rectangle(length, breadth)
print(f'Area of Rectangle is {res}')  
