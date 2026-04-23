#############################################################################
                              #Day28 Practice
#############################################################################

#QUESTION SMALLEST INDEX WITH DIGIT SUM EQUAL TO INDEX
nums=eval(input("enter list of integrs"))
lis=[]
for i in range(len(nums)):
    sum1=0
    for j in str(nums[i]):
        sum1+=int(j)
        if sum1==i:
            lis.append(sum1)
if len(lis)!=0:
    print(min(lis))
else:
    print(-1)