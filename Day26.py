#############################################################################
                              #Day26 Practice
#############################################################################

#QUESTION  Count Digit Appearances

nums=eval(input("enter list of integrs"))
digit=int(input("enter digit"))
count=0
num="".join(map(str,nums))
for i in num:
    if i==str(digit):
        count+=1
print(count)