#############################################################################
                              #Day45  Practice
#############################################################################

#question . Sum of Square Numbers
import math
c=int(input("enter c"))
start=0
end=int(math.sqrt(c))
for i in range(start,end+1):
    if start**2+end**2==c:
        print(True)
        break
    elif start**2+end**2>c:
        end-=1
    else:
        start+=1
else:
    print(False)