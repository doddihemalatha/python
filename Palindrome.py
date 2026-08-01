num = abs(int(input("Enter a number:")))

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
