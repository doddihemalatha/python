num = int(input("Enter a Number:"))

original = num
count = 0

while num > 0:
    count+=1
    num = num//10
print(count)

num = original
total = 0 

while num > 0:
    last_digit = num%10
    power = last_digit**count
    total= total+power
    num = num//10
    
if original = total:
    print("Arm Strong Number")
else:
    print("Not Arm Strong Number")
