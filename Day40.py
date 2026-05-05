#############################################################################
                              #Day40  Practice
#############################################################################

#question SUM OF SQUARES OF SPECIAL ELEMENTS
nums=eval(input("enter list of integers"))
lis=[]
l=len(nums)
for i in range(len(nums)):
    if l%(i+1)==0:
        lis.append(nums[i])
lis2=[]
for i in lis:
    lis2.append(i*i)
print(sum(lis2))
        