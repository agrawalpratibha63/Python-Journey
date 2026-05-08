#############################################################################
                              #Day43  Practice
#############################################################################

#question Uncommon Words from Two Sentences
s1=input("enter string")
s2=input("enter string 2")
lis=[]
s=s1.split()
sn=s2.split()
new=s + sn
for i in new:
    if new.count(i)==1:
        lis.append(i)
print(lis)