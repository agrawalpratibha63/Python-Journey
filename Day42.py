#############################################################################
                              #Day42  Practice
#############################################################################

#QUESTION Divisible and Non-divisible Sums Difference

n=int(input("enter n"))
m=int(input("enter m"))
num1=[]
num2=[]
for i in range(1,n+1):
    if i%m!=0:
        num1.append(i)
    else:
        num2.append(i)
n1=sum(num1)
n2=sum(num2)
print(n1-n2)