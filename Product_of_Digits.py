num = abs(int(input("Enter a Number:")))

product = 1

if num ==0:
    print("The Product is:0")
else:
    while num > 0:
        last_digit = num%10
        product = product*last_digit
        num = num//10
      
    print("-"*20)
    print("The product is:",product)
