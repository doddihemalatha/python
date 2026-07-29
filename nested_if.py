age = int(input("Enter Your Age:"))

if age >=18:
    
    had_id = input("Do you have id:").lower()

    if had_id == 'yes':
        print("entry allowed")
    elif had_id == 'no':
        print("Bring ID proof")
    else:
        print("Invalid enter only yes or no")
        
else:
    print("Not Eligible")
