#############################################################################
                              #Day48  Practice
#############################################################################

#Question Set Mismatch

nums = [1,2,2,4]
lis=[]
for i in nums:
    if nums.count(i)>1:
        lis.append(i)
        break
for i in range(1,len(nums)+1):
    if i not in nums:
        lis.append(i)
        break
print(lis)