gender=input("Enter Gender(M/F):")
age=int(input("Enter age:"))
if(gender=='F'): 
    if(age>=18):
        print("Girl is Eligible for marriage.")
    else:
        print('Girl is not Eligible for marriage.')
else:
    if(age>=21):
        print('Boy is Eligible for marriage.')
    else:
        print('Boy is not Eligible for marriage.') 