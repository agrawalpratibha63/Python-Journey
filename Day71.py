####################################################################
                     #DAY70 PRACTICE
####################################################################

#QUESTION   Exams
T=int(input("enter testcases:"))
for i in range(T):
    x,y,z=map(int,input("enter numbers:").split())    
    p=x*y
    perc=(z/p)*100
    if perc>50:
        print("YES")
    else:
        print("NO")