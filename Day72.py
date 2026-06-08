########################################################################################
                                 #DAY 72 PRACTICE
########################################################################################

#QUESTION Qualify the round

T=int(input("ENTER TESTCASES:"))
for i in range(T):
    x,a,b=map(int,input("ENTER:").split())    
    p=(a*1)+(b*2)
    if p>=x:
        print("Qualify")
    else:
        print("NotQualify")