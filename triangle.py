print("Enter the sides")
a=int(input())
b=int(input())
c=int(input())
if a**2==b**2+c**2:
    print("Right angle triangle")
if b**2==a**2+c**2:
    print("Right angle triangle")
if c**2==a**2+b**2:
    print("Right angle triangle")
else:
    print("Not a right angle triangle")
