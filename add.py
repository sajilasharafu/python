print(" 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division")
n=int(input("Enter your choice:"))
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if n==1:
    sum=a+b
    print("Sum is:",sum)
elif n==2:
    sub=a-b
    print("diffrence is:",sub)
elif n==3:
    mul=a*b
    print("mul is:",mul)
elif n==4:
    div=a/b
    print("div is:",div)
else:
    print("Invalid number")
