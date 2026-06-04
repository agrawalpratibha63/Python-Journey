#############################################################################
                              #Day67  Practice
#############################################################################
   
#Question  Sale Season

T=int(input("enter testcases:"))
for i in range(T):
    x=int(input("enter integer:"))
    if x<=100:
        print(x)
    elif 100<x<=1000:
        print(x-25)
    elif 1000<x<=5000:
        print(x-100)
    else:
        print(x-500)