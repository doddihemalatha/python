#Right_Aligned_Half_Pyramid

for row in range(1,6):                             
    for space in range(5-row):
        print(" ",end="")
    for star in range(1,row+1):
            print("*",end="")
    print()
