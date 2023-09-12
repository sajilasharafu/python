print("Enter the marks")
m1=int(input())
m2=int(input())
m3=int(input())
avg=(m1+m2+m3)/3
if avg>=91 and avg<=100:
    print("Grade is A")
elif avg>=81and avg<91:
    print("Grade is B")
elif avg>=61 and avg<81:
    print("Grade is C")
elif avg>=41 and avg<61:
    print("Grade is D")
elif avg>=0 and avg<41:
    print("Grade is E")
else:
    print("Invalid input")
