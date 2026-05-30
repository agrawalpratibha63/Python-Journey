#############################################################################
                              #Day64  Practice
#############################################################################

#Question  Count the Notebooks
try:
    T=int(input("enter testcases:"))
    for i in range(T):
        x=int(input("enter:"))
        p=(x*1000)//100
        print(p)
except ValueError:
    print("enter valid value...")