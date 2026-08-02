num1 = int(input("Enter 1st Number:"))
num2 = int(input("Enter 2nd Number"))

if num1 < num2:
    small = num1
else:
    small = num2
 
x = 1
gcd = 1

while x <= small:
    if num1%x==0 and num2%x==0:
        gcd = x
    x+=1
print("GCD =",gcd)
