a=int(input("Enter value of a"))
b=int(input("Enter value of b"))
c=int(input("Enter value of c"))
d=b**2-4*a*c
d1=d**0.5
if(d<0):
    print("The roots are imaginary")
else:
    r1=(-b+d1)/2*a
    r2=(-b-d1)/2*a
    print("The first root: "r1)
    print("The first root: "r2)
