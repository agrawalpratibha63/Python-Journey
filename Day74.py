####################################################################
                     #DAY74 PRACTICE
####################################################################

#QUESTION Police and Thief
T=int(input("enter testcases:"))
for i in range(T):
    a,b=map(int,input("enter:").split())  
    print(abs(a-b))