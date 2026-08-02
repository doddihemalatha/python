num = int(input("Enter a Number:"))

x=1
total = 0
original = num

while x<num:
    if num%x==0:
        total = total + x
    x+=1
    
if original == total:
    print("Perfect Number")
else:
    print("Not Perfect Number")
