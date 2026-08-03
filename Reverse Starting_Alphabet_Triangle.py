

for row in range(1, 6):

    start = 70 - row
    for letter in range(start, 70):
        print(chr(letter), end="")

    print()


         #or

for row in range(1, 6):

    start = 70 - row

    while start <= 69:
        print(chr(start), end="")
        start += 1
    print()
