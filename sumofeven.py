n = int(input("Enter the number"))
sum = 0
while n > 0:
    dig = n % 10
    if dig % 2 == 0:
        sum += dig
    n = n//10
print("sum is : ", sum)