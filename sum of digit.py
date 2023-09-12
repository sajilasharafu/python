n=int(input("Enter the number"))
sum=0
while n>0:
    dig=n%10
    sum=sum+dig
    n=n//10
    if n==0 and sum>9:
        n=sum
        sum=0
print("sum",sum)