#############################################################################
                              #Day23 Practice
#############################################################################

#Question  Split Strings by Separator
words=eval(input("enter list pf strings:"))
separator=input("enter separator")
lis=[]
for word in words:
    p=word.split(separator)
    for i in p:
        if i=="":
            continue
        else:
            lis.append(i)
print(lis)