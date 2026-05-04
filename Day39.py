#############################################################################
                              #Day38 Practice
#############################################################################

#QUESTION ROTATE THE STRING
nums=eval(input("enter list"))
k=int(input())
for i in range(k):
    p=nums.pop()
    nums.insert(0,p)
print(nums)