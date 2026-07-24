#movie ticket booking using if-else

ticket_price=200
no_of_tickets=int(input("Enter Number of Tickets:"))
total_price=ticket_price*no_of_tickets

if total_price>=1000:
    print("Congratulations!\nYou got free popcorn")
else:
    print("No Free Popcorn")
print("Total Bill:",total_price)
