#############################################################################
                              #Day52  Practice
#############################################################################

#Question  Adding Spaces to a String

s=input("enter the string:")
spaces=eval(input("enter the list:"))
s1=[]
left=0
n=len(spaces)
for i in range(len(s)):
    if left<n and i==spaces[left]:
        s1.append(" "+s[i])
        left+=1
    else:
        s1.append(s[i])
m="".join(s1)
print(m)
            