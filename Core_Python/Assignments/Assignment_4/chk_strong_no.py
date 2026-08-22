num=int(input("Enter a number: "))
temp=num
sum=0
while temp>0:
    digit=temp%10

    fact=1
    for i in range(1,digit+1):
        fact=fact*i 
    sum=sum+fact
    temp//=10

if sum==num:
    print(f'{num} is a strong number')
else:
    print(f'{num} is not a strong number')