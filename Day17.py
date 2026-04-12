##################################################################
                   #Day 17 practice
##################################################################

#QUESTION: . Minimum Average of Smallest and Largest Elements

nums=eval(input("enter list of elements:"))
averages=[]
while nums!=[]:
    m=max(nums)
    m1=min(nums)
    res=(m+m1)/2
    averages.append(res)
    nums.remove(m)
    nums.remove(m1)
print(min(averages))