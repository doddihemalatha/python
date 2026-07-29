age = int(input("Enter Your Age:"))

if age >=18:
    
    has_id = input("Do you have ID:").lower()
    if has_id == 'yes':
        no_of_days = int(input("Enter Number of days:"))
        room_charge=1500
        total_room_charge = no_of_days*room_charge
        print("-"*20)
        print("check-in Successful")
        print("Days Stayed :",no_of_days)
        print("Room Charge per day :",room_charge)
        print("Total Bill:",total_room_charge )
        if total_room_charge >=10000:
            print("Congratulations!\nFree Breakfast Included")
    elif has_id == 'no':
        print("Check-in Rejected\nValid ID Required")
    else:
        print("Invalid")
else:
    print("Check in not allowed")
