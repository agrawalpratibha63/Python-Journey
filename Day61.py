#############################################################################
                              #Day61  Practice
#############################################################################

#Question  Flip the cards

T=int(input("enter no of testcases:"))
for i in range(T):
    n,x=map(int,input("enter:").split())  
    print(min(x,n-x))