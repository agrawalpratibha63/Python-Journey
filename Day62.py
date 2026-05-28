#############################################################################
                              #Day62  Practice
#############################################################################

#Question Air Conditioner Temperature

T=int(input("enter the testcases:"))
for i in range(T):
    a,b,c=map(int,input("enter:").split())    
    if b>=a and b>=c:
        print("YES")
    else:
        print("NO")
