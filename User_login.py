username = input("Enter your Name:").lower()

if username == 'hema':
    password = input("enter password:")
    if password == 'python123':
        otp = int(input("Enter OTP:"))
        if otp == 5678:
            print("Login Successful")
        else:
            print("Invalid OTP")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")
