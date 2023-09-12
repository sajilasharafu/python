num=int(input("Enter a number"))
temp=num
sum=0
while num>0:
    dig=num%10
    fact=1
    i=1
    while i<=dig:
        fact=fact*i
        i+=1
    sum=sum+fact
    num=num//10
if temp==sum:
    print("strong number")
else:
    print("Not a strong number")