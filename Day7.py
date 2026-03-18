#=============================================================
                        #Day7 Pattern practice
#=============================================================

# *
# **
# ***
# ****
r=int(input("enter no of rows:"))
for i in range(r):
    for j in range(i+1):
        print("*",end=" ")
    print()
# ****
# ***
# **
# *
n=int(input("enter no of rows:"))
for i in range(n):
    for j in range(n,0,-1):
        print("*",end=" ")
    print()
    n=n-1
# 1
# 12
# 123
# 1234
r=int(input("enter no of rows:"))
for i in range(1,r+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
# A
# BB
# CCC
# DDDD
n=int(input("enter no of rows:"))
a=65
for i in range(1,n+1):
    for j in range(1,i+1):
        ch=chr(a)
        print(ch,end=" ")
    print()
    a=a+1
# A
# AB
# ABC
# ABCD
n=int(input("enter no of rows:"))
for i in range(1,n+1):
    a=65
    for j in range(1,i+1):
        ch=chr(a)
        print(ch,end=" ")
        a=a+1
    print()
# 1
# 22
# 333
# 4444
n=int(input("enter no of rows:"))
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()

    

    


