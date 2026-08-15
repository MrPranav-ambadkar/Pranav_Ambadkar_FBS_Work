cp=float(input("Enter the cost price: "))
sp=float(input("Enter the selling price: "))
if sp>cp:
    profit=sp-cp
    print(f'Profit is: {profit}')
elif cp>sp:
    loss=cp-sp
    print(f'Loss is: {loss}')
else:
    print("No profit no loss")