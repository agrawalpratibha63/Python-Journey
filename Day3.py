#=====================================================
                    #Day3- Basic questions
#=====================================================

#ques1. Smart temp conversion in Fahrenheit and kelvin

celsius=int(input("Enter temp in celsius:"))
Fahrenheit=9/5*celsius+32
kelvin=celsius+273.15
print("Temp in Fahrenheit:",Fahrenheit)
print("Temp in kelvin:",kelvin)

#Ques2. Write a program to read numbers and print their quotient and remainder.

num1=int(input("enter Num1:"))
num2=int(input(" enter Num2:"))
r1=num1%num2
q1=num1/num2
print("Quotient is:",q1)
print("Remainder is:",r1)

#ques3. write a program to compute simple interest and compound interest.
p=int(input("Enter principal amount:"))
r=int(input("Enter rate:"))
t=int(input("Enter time(in yrs):"))
si=p*r*t/100
print("Simple interest is:",si)
n=int(input("Number of times interest is compounded:"))
r_decimal=r/100
a=p*(1+r_decimal/n)**(n*t)
ci=a-p
print(f"Compound interest is:{ci:.2f}")

