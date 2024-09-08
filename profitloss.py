actualpay=float(input("enter an actual amount"))
sell=float(input("sell amount"))
profit=sell-actualpay 
if profit>0:
    print(profit,"is the profit")
else:
    print("loss")