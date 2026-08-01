num = abs(int(input("Enter Number: ")))

if num == 0:
    print("Number of Digits: 1")
else:
    count = 0

    while num > 0:
        num = num // 10
        count += 1

    print("Number of Digits:", count)
