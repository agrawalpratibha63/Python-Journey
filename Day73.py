########################################################################################
                                 #DAY 73 PRACTICE
########################################################################################

#QUESTION  Jenga Night

T=int(input("enter testcases:"))
for i in range(T):
    a,b=map(int,input("enter:").split())   
    if b%a==0:
        print("YES")
    else:
        print("NO")