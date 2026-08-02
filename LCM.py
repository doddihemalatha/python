num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))


if num1 > num2:
    x = num1
else:
    x = num2

while True:
    if x % num1 == 0 and x % num2 == 0:
        print("LCM =", x)
        break
    x += 1
