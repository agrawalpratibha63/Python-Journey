#############################################################################
                              #Day52  Practice
#############################################################################

#Question  Search in Rotated Sorted Array
nums=eval(input("enter list of integers:"))
target=int(input("enter taregt value:"))
for i in nums:
        if target in nums:
            print(nums.index(target))
            break
        else:
             print(-1)