import random

CORRECT_USERID = "admin"
CORRECT_PASSWORD = "password123"

userid = input("Enter User ID: ")
password = input("Enter Password: ")

if userid == CORRECT_USERID and password == CORRECT_PASSWORD:
    print("\nLogin successful!")
    
    captcha_code = random.randint(1000, 9999)
    print(f"CAPTCHA Code: {captcha_code}")
    
    user_captcha = input("Enter the 4-digit number displayed above: ")
    
    if user_captcha.isdigit() and int(user_captcha) == captcha_code:
        print("\nSuccess: Verification complete!")
    else:
        print("\nFailed: Incorrect CAPTCHA entered.")

else:
    print("\nFailed: Invalid User ID or Password.")