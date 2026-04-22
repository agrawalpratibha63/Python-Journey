#############################################################################
                              #Day27 Practice
#############################################################################

#question Find Closest Person

x=int(input("enter x"))
y=int(input("enter y"))
z=int(input("enter z"))
p1=z-x
p2=z-y
if abs(p1)<abs(p2):
    print(1)
elif abs(p2)<abs(p1):
    print(2)
else:
    print(0)