#students marks grade

marks=int(input("Enter your Marks:"))

if marks<0 or marks>100:
    print("Invalid Marks")
elif marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=50:
    print("Grade C")
elif marks>=35:
    print("Grade D")
else:
    print("Fail")
