#############################################################################
                              #Day52  Practice
#############################################################################

#Question Neither Minimum nor Maximum
nums=eval(input("enter list of integers:"))
m=min(nums)
p=max(nums)
for i in range(len(nums)):
    if nums[i]!=m and nums[i]!=p:
        print(nums[i])
        break
    else:
        continue
else:
    print(-1)