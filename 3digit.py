n=int(input("Enter digit number : "))
a=int(input("Enter the first digit : "))
while n>0:
    dig = n % 10
    n = n // 10
if a==dig:
    print("start with",a)
else:
    print("not start with",a)
