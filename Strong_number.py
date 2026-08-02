num = int(input("Enter a Number:"))

original = num 
x=1
factorial = 1 
total = 0 

while num> 0:
    last_digit= num%10
    x=1
    factorial = 1 
    while x<=last_digit:
        factorial = factorial * x
        x+=1
    total = total+factorial
    num = num//10
print(total)

if total == original:
    print("Strong Number")
else:
    print("Not a Strong Number")
