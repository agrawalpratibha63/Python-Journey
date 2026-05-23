#############################################################################
                              #Day58  Practice
#############################################################################

#Question Car or Bike

T=int(input("enter no of testcases"))
for i in range(T):
    a,b=map(int,input("enter:").split()) 
    if a>b:
        print("CAR")
    elif b>a:
        print("BIKE")
    else:
        print("SAME")
