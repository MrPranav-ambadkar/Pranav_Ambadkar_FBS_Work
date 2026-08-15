id=input("Enter your User ID: ")
pwd=input("Enter your Password: ")
if id=="admin" and pwd=="1234":
    print("Login Successful")   
elif id=="admin" and pwd!="1234":
    print("Invalid Password")
elif id!="admin" and pwd=="1234":
    print("Invalid User ID")
elif id!="admin" and pwd!="1234":
    print("Invalid User ID and Password")
else:
    print("Invalid User ID and Password")