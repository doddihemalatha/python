num = abs(int(input("Enter a Number")))

x = 1
count = 0

while x <= num:
    if num % x == 0:
        count+=1
    x+=1
  
if count == 2:
    print("Prime Number")
else:
    print("Not Prime Number")
