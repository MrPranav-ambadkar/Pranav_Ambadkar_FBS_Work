sub1=float(input("Enter marks of subject 1: "))
sub2=float(input("Enter marks of subject 2: "))
sub3=float(input("Enter marks of subject 3: ")) 
sub4=float(input("Enter marks of subject 4: "))
sub5=float(input("Enter marks of subject 5: "))

total=sub1+sub2+sub3+sub4+sub5
percentage=(total/500)*100

if percentage>=75:
    print("First Class with Distinction")
elif percentage>=60:
    print("First Class")
elif percentage>=45:
    print("Second Class")
else:
    print("Failed")