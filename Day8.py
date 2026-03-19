#==========================================================
                        #DAY8 STRING PRACTICE
#==========================================================

# QUES1 Secure password analyzer
str=input("enter password:")
for i in range(len(str)):
    if str.count(str[i])>=3:
        print("Weak password")
        break
else:
    print("Strong password")