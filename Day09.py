#==================================================================
                         #Day9 String Practice
#==================================================================

#Mirror String Validator
str=input("enter the string")
mid=len(str)//2
first_half=str[:mid]
sec_half=str[mid:]
if first_half[::-1]==sec_half:
    print("Yes mirror string")
else:
    print("Not mirror string")


