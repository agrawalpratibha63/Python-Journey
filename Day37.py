#############################################################################
                              #Day37 Practice
#############################################################################

#QUESTION  Rearrange Array Elements by Sign
nums=eval(input("enter list of integers:"))
lis1=[]
lis2=[]
for i in nums:
    if i>0:
        lis1.append(i)
    else:
        lis2.append(i)
flattened = [item for pair in zip(lis1, lis2) for item in pair]
print(flattened)