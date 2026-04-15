#################################################################
                      #Day20 practice
#################################################################


#Question  Earliest Time to Finish One Task
tasks=eval(input("enter list ofintegers:"))
lis=[]
for row in tasks:
    sum1=0
    for element in row:
        sum1+=element
    lis.append(sum1)
print(min(lis))