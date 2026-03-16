#====================================================
                  #Day 5 For loops Practice
#====================================================

#Ques1. wap that takes exactly four for loops to print the sequence of letters below:
#A A A A A A A A A A B B B B B B B C C C C C C E E E E E

for a in range(1,11):
    print("A",end=" ")
for a in range(1,8):
    print("B",end=" ")
for a in range(1,7):
    print("C",end=" ")
for a in range(1,6):
    print("D",end=" ")

#QUES2. WAP That checks in the range 1....100 and prints "Fizz" if the number is multiple of 3 and prints "Buzz" if the number is multiple of 5. It should print "FizzBuzz" if the number is both multiple of 3 and 5.

for i in range(1,101):
    if i %3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
else:
    print("Invalid number. Out of range!")
