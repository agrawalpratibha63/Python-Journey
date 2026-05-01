#############################################################################
                              #Day36 Practice
#############################################################################

#question  Remove Zeros in Decimal Representation
n=int(input("ENTER VALUE"))
lis=[]
nums=list(map(int,str(n)))
for i in nums:
    if i!=0:
        lis.append(str(i))
s="".join(lis)
print(int(s))