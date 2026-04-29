#############################################################################
                              #Day28 Practice
#############################################################################

#question  Minimum Common Value
nums1=eval(input("enter:"))
nums2=eval(input("enter2:"))
s1=set(nums1)
s2=set(nums2)
s3=s1.intersection(s2)
if len(s3)!=0:
    print(min(s3))
else:
    print(-1)