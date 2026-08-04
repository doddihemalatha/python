
for row in range(1,6):
    for space in range(row-1):
        print(" ",end="")
    for star in range(11-2*row):
        print("*",end="")
    print()
