num = int(input("Enter a number: "))
if(num<0):
    if num % 2 == 0:
        print("Negative Even number")
    else:
        print("Negative Odd number")
elif num==0:
    print("Zero")
else:
    if num % 2 == 0:
        print("Positive Even number")
    else:
        print("Positive Odd number")
