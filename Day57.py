#############################################################################
                              #Day52  Practice
#############################################################################

#Question The Two Sneaky Numbers of Digitville
nums=eval(input("enter list of integers:"))
lis=[]
s=set(nums)
for i in s:
    if nums.count(i)==2:
        lis.append(i)
    else:
        continue
print(lis)