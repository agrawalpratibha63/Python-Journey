#############################################################################
                              #Day60  Practice
#############################################################################

#Question Minimum Cars required

T=int(input("enter no of testcases:"))
for i in range(T):
    x=int(input("enter no.:"))
    if x%4==0:
        print(x//4)
    else:
        print((x//4)+1)