number = 1

for row in range(5, 0, -1):
    for num in range(1, row + 1):
        print(number, end="")
    print()
    number += 1
