###################################################################
                      #Day22 practice
###################################################################

#Question . Element Appearing More Than 25% In Sorted Array

arr=eval(input("enter list of integers:"))
length=len(arr)
for i in range(len(arr)):
    c=arr.count(arr[i])
    if (c/length)>0.25:
        print(arr[i])
        break