
for row in range(1,6):
    for space in range(5-row):
        print(" ",end="")
    for increasing in range(1,row+1):
        print(increasing,end="")
    for decreasing in range(row-1,0,-1):
        print(decreasing,end="")
    print()
