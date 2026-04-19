#############################################################################
                              #Day24 Practice
#############################################################################

#QUESTION . First Matching Character From Both Ends
s=input("enter string")
length=len(s)
left=0
right=length-1
while left<=right:
    if s[left]==s[right]:
        print(left)
        break
    left+=1
    right-=1
else:
    print("-1")