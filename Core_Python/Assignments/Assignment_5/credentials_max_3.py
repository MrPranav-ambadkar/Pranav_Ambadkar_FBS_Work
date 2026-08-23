correct_user_id = "admin"
correct_password = "1234"

for attempt in range(3):
    user_id = input("Enter your user ID: ")
    pwd = input("Enter your password: ")

    if user_id == correct_user_id and pwd == correct_password:
        print("Login successful")
        break
    else:
        print("Invalid User ID or Password")

else:
    print("You have exceeded 3 attempts. Program terminated.")