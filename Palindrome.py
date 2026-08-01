num = int(input("Enter a number:"))

if num <0:
    print("  not palindrome")
else:
    original = num
    reverse = 0


    while num>0:
        last_digit = num%10
        reverse = reverse * 10 + last_digit
        num = num // 10

    if original == reverse:
        print("Palindrome")
    else:
        print("Not palindrome")
