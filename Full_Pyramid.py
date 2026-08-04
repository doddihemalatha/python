

for row in range(1,6):
    for space in range(5-row):
        print(" ",end="")
    for star in range(row*2-1):
        print("*",end="")
    print()
