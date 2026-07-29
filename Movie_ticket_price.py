adult_ticket_price = 200
child_ticket_price = 100

age = int(input("Enter Your Age:"))
no_of_tickets=int(input("Enter Number of tickets:"))

if age<=0 or no_of_tickets<=0:
    print("Invalid")
elif age<5:
    print("free Ticket")
elif age>=5 and age<=17:
    print("Child ticket",child_ticket_price)
    total_price=no_of_tickets*child_ticket_price
    print("Total Price",total_price)
    
    if total_price>=1000:
        print("Congratulations! You got FREE Popcorn.")
else:
    print("Adult Ticket",adult_ticket_price)
    total_price=no_of_tickets*adult_ticket_price
    print("Total Price",total_price)
    
    if total_price>=1000:
        print("Congratulations! You got FREE Popcorn.")
