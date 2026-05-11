#############################################################################
                              #Day46  Practice
#############################################################################

#Question  . Richest Customer Wealth
accounts=eval(input("enter list of integers"))
lis=[]
for l in accounts:
    s=sum(l)
    lis.append(s)
mx=max(lis)
print(mx)