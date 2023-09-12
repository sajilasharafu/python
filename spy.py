n=int(input("Enter the number "))
sum=0
mul=1
while n>0:
    dig=n%10
    sum=sum+dig
    mul=mul*dig
    n=n//10
if sum==mul:
    print("Spy number")
else:
    print("Not a spy number")