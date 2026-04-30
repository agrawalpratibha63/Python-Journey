#############################################################################
                              #Day35 Practice
#############################################################################

#question Three Consecutive Odds
arr=eval(input("enter list of integers"))
for i in range(len(arr)-2):
    if arr[i]%2!=0 and arr[i+1]%2!=0 and arr[i+2]%2!=0:
        print(True)
else:
    print(False)