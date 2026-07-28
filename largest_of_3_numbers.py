num1=float(input("Enter first Number:"))
num2=float(input("Enter second number:"))
num3=float(input("Enter Third number:"))

if num1>num2 and num1>num3:
    print("First number is larger",num1)
elif num2>num1 and num2>num3:
    print("second number is larger",num2)
elif num3>num1 and num3>num2:
    print("Third number is larger",num3)
elif num1==num2 and num1>num3:
    print("First and Second number are larger")
elif num1==num3 and num1>num2:
    print("First and third number is larger")
elif num2==num3 and num2>num1:
    print("Second and Third number is larger")
else:
    print("All numbers are equal")
