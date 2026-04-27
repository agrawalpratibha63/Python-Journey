#############################################################################
                              #Day28 Practice
#############################################################################

#Question Capitalize the Title

title=input("enter string ")
lis=[]
s=title.split()
for i in s:
    if len(i)>=3:
        lis.append(i.title())
    else:
        lis.append(i.lower())
m=" ".join(lis)
print(m)
        