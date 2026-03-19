#ques1.
# str=input("enter password:")
# for i in range(len(str)):
#     if str.count(str[i])>=3:
#         print("Weak password")
#         break
# else:
#     print("Strong password")
#ques2.Mirror string validator
# s=input("enter the string")
# mid=len(s)//2
# first_half=s[:mid]
# sec_half=s[mid:]
# if first_half[::-1]==sec_half:
#     print("Mirror String")
# else:
#     print("Not Mirror String")
#ques3. Longest Unique substring
s1=input("Enter string:")
count=1
for i in range(len(s1)-1):
    if s1[i]==s1[i+1]:
        count=1
    else:
        count+=1
print(count)





