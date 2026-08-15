s1=int(input("Enter the first side of triangle: "))
s2=int(input("Enter the second side of triangle: "))
s3=int(input("Enter the third side of triangle: "))
if s1+s2>s3:
    print("The triangle is a isosceles triangle")
elif s2+s3>s1:
    print("The triangle is a scalene triangle")
elif s1+s3>s2:
    print("The triangle is a equilateral triangle")
else:
    print("The triangle is not valid")