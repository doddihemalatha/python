
alphabet = 65

for row in range(1,6):
    for num in range(1,row+1):
        print(chr(alphabet),end=" ")
        alphabet+=1
    print()
