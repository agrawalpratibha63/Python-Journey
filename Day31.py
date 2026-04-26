#############################################################################
                              #Day28 Practice
#############################################################################

#Question Check if Numbers Are Ascending in a Sentence

s=input("enter a string")
lis=[]
new=s.split()
for i in range(len(new)):
    if new[i].isdigit():
        lis.append(int(new[i]))
    else:
        continue
count=0
for i in range(len(lis)-1):
    if lis[i]<lis[i+1]:
        count+=1
if count==len(lis)-1:
    print(True)
else:
    print(False)

        