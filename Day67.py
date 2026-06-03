#############################################################################
                              #Day67  Practice
#############################################################################
   
#Question  Greater Average

T=int(input())
for i in range(T):
    a,b,c=map(int,input().split())  
    if ((a+b)/2)>c:
        print("yes")
    else:
        print("no")
