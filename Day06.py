#============================================
            #Day6 for loops pattern practice
#============================================

#Ques1. Print this pattern 

# ****
# ***
# **
# *
n=int(input("enter number of rows:"))
for i in range(n):
    for j in range(n,0,-1):
        print("*",end=" ")
    print()
    n=n-1
