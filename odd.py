a=int(input("Enter the range from : "))
n=int(input("Enter the limit : "))
while a<=n:
    if a%2!=0:
        print(a," is Odd")
    else:
        print(a," is Even")
    a+=1