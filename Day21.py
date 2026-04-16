########################################################################
                              #Day21 practice\
########################################################################

#ques Minimum Distance to the Target Element
target=int(input("enter target value"))
start=int(input("enter start value:"))
nums=eval(input("enter list of integers:"))
lis=[]
for i in range(len(nums)):
    if nums[i]==target:
        lis.append(abs(i-start))
        continue
print(min(lis))
