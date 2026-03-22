#=========================================================
         # Conditional statements and loops#
#=========================================================
 
#ques1. Print the Fibonacci series up to n terms where n is provided by the user.

n=int(input("enter upto which terms you want:"))
a=0
a1=a
b=1
for i in range(n):
    if i==n-1:
        print(a)
    else:
        print(a,end=',')
        c=a+b
        a=b
        b=c
   
