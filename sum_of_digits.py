num = abs(int(input("Enter a Number:")))

sums = 0

while num > 0:
    last_digit = num%10
    sums = sums+last_digit
    num = num//10
  
print("-"*20)
print("The sum of digits is",sums)
