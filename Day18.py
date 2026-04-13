#######################################################################
                    #day 18 practice
#######################################################################

#Question Plus one
digits=eval(input("enter:"))
rev=0
for i in digits:
    rev=(rev*10)+i
    n=rev
    s=n+1
    lis=list(map(int,str(s)))
print(lis)