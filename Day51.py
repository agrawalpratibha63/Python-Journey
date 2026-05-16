#############################################################################
                              #Day50  Practice
#############################################################################

#Question Restore Finishing Order
order=eval(input("1:"))
friends=eval(input("2:"))
lis=[]
for i in order:
    if i in friends:
        lis.append(i)
print(lis)