#############################################################################
                              #Day50  Practice
#############################################################################

#Question Hammming Distance

x=int(input("enter x:"))
y=int(input("enter y:"))
a=bin(x)[2:]
b=bin(y)[2:]
max_len=max(len(a),len(b))
p=a.zfill(max_len)
q=b.zfill(max_len)
num1=list(map(int,str(p)))
num2=list(map(int,str(q)))
count1=0
for i in range(len(num1)):
    if num1[i]!=num2[i]:
        count1+=1
print(count1)