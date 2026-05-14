#############################################################################
                              #Day49  Practice
#############################################################################

#Question single number 2
nums = eval(input("enter list:"))

for i in nums:
    if nums.count(i) == 1:
        print(i)
        break
else:
    # Yeh tabhi chalega jab pura loop bina break ke khatam ho jaye
    print(-1)