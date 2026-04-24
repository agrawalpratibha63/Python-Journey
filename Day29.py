#############################################################################
                              #Day28 Practice
#############################################################################

#QUESTION  Maximum Sum With Exactly K Elements

nums=eval(input("enter list of integrs"))
k=int(input("enter value of k"))
numbers=sorted(nums)
sum1=0
p=numbers.pop()
while k>0:
    sum1+=p
    p=p+1
    k=k-1
print(sum1)