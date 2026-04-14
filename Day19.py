#############################################################################
                                #Day19 Practice
#############################################################################

#Question Separate the digits in an Array

nums=eval(input("Enter list of integers:"))
lis=[]
for i in nums:
    a=map(int,str(i))
    for i in a:
        lis.append(i)
print(lis)