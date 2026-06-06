####################################################################
                     #DAY70 PRACTICE
####################################################################

#QUESTION  Monopoly
T=int(input("ENTER TESTCASES:"))
for i in range(T):
    a,b,c,d=map(int,input("ENTER NUMBER").split())  
    if a>(b+c+d) or b>(a+c+d) or c>(a+b+d) or d>(a+b+c):
        print("YES")
    else:
        print("NO")