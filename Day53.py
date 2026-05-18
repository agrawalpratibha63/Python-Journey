#############################################################################
                              #Day52  Practice
#############################################################################

#Question Search in Rotated Sorted Array II

nums=eval(input("enter list of integers"))
target=int(input("enter target value:"))
s=sorted(nums)
if target in s:
    print(True)
else:
    print(False)