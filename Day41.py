#############################################################################
                              #Day41  Practice
#############################################################################

#QUESTION  Fair Candy Swap
aliceSizes=eval(input("enter"))
bobSizes=eval(input("enter2"))
a=sum(aliceSizes)
b=sum(bobSizes)
c=(a-b)//2
for i in aliceSizes:
    for j in bobSizes:
        if i-j==c:
            print([i,j])
            break
    else:
        continue
    break

        