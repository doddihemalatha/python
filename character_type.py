character=input("enter character:")

if len(character)!=1:
    print("Invalid")
elif character.isalpha():
    print("Alphabet")
elif character.isdigit():
    print("Digit")
else:
    print("Special Character")
