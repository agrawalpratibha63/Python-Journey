#############################################################################
                              #Day28 Practice
#############################################################################

#QUESTION Count of Matches in Tournament
n=int(input("enter value of n"))
lis=[]
while n!=1:
    if n%2==0:
        matches=n/2
        n=n/2
        lis.append(matches)
    else:
        matches=(n-1)/2
        n=((n-1)/2)+1
        lis.append(matches)
print(int(sum(lis)))

        

