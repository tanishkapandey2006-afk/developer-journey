#print numbers from 1-10 using while loop
i = 1
while i <= 10:
    print(i)
    i += 1
#print numbers from 10-1 using while loop
i = 10
while i >= 1:
    print(i)
    i -= 1
#print multiplication table of a number
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1
#get user input and keep adding until user enters 0
sum=0
while True:
    n = int(input("Enter a number: "))
    if(n==0):
        break
    sum+=n
print(sum)
