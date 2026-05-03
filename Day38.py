#############################################################################
                              #Day38 Practice
#############################################################################

#QUESTION   Two Out of Three
nums1=eval(input("enter list of integers:"))
nums2=eval(input("enter list of integers2:"))
nums3=eval(input("enter list of integers3:"))
lis=[]
n=nums1+nums2+nums3
num=set(n)
new=list(num)
for i in new:
    if (i in nums1 and i in nums2) or (i in nums2 and i in nums3) or (i in nums1 and i in nums3):
        lis.append(i)
    else:
        continue
print(lis)   