#############################################################################
                              #Day28 Practice
#############################################################################

#QUESTION  Median of Two Sorted Arrays
nums1=eval(input("enter:"))
nums2=eval(input("enter2:"))
p=nums1+nums2
q=sorted(p)
if len(q)%2==0:
    l=(len(q)//2)
    m=(len(q)//2)+1
    res=(q[l-1]+q[m-1])/2
    print(res)
else:
    l=(len(q)+1)//2
    res=q[l-1]
    print(res)

        