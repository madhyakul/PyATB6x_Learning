# guess number is even or odd
num = int(input("Enter number: "))
if num>=0:
    if num%2==0:
        print("Number is even")
    else:
        print("Number is odd")
else:
    print("Number is negative")

if num>=0:
    print("Number is Even" if num%2==0 else "Number is Odd")