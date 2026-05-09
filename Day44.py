#############################################################################
                              #Day43  Practice
#############################################################################

#question Count Good Triplets
arr=eval(input("enter list of integers"))
a=int(input("enter a "))
b=int(input("enter b"))
c=int(input("enter c "))
lis=[]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
              if (abs(arr[i]-arr[j])<=a) and  (abs(arr[j]-arr[k])<=b) and (abs(arr[i]-arr[k])<=c):
                    lis.append((arr[i],arr[j],arr[k]))
              else:
                  continue
print(len(lis))
