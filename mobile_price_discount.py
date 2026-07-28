mobile_price=int(input("Enter mobile price:"))
student=input("Are you a Student:").lower()

if mobile_price>=50000 and student=='yes':
    discount_percentage=15
    discount_amount=mobile_price*15/100
    final_price=mobile_price-discount_amount
    print("Congratulation you got 15% Discount")
    print("-"*20)    
    print("Original Price:",mobile_price)
    print("Discount Amount",discount_amount)
    print("Final Price:",final_price)
    
elif mobile_price>=50000 and student=='no':
    discount_percentage=10
    discount_amount=mobile_price*10/100
    final_price=mobile_price-discount_amount
    print("Congratulation you got 10% Discount")
    print("-"*20)    
    print("Original Price:",mobile_price)
    print("Discount Amount",discount_amount)
    print("Final Price:",final_price)
    
elif student!="yes" and student!="no":
    print("Invalid!")
    print("Please enter only yes or no")
else:
    print("No Discount")
    print("Original Price:",mobile_price)
    print("Final Price:",mobile_price)
    
