num=int(input("Enter a number of terms: "))
a,b=0,1
print("Fibonacci series:")
for i in range(num):
    print(a)
    c=a+b
    a=b
    b=c
