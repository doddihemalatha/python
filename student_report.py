#student report

print("-"*10,"Student Report","-"*10)

english=float(input("Enter English Marks:"))
maths=float(input("Enter Maths Marks:"))
science=float(input("Enter Science Marks:"))
social=float(input("Enter Social Marks:"))
computer=float(input("Enter Computer Marks:"))

print("-"*50)

#to print all subject marks, total and average

print("English : ",english,"\nMaths : ",maths,"\nScience : ",science,"\nSocial : ",social,"\nComputer : ",computer)
total_marks=english+maths+science+social+computer
average=total_marks/5

print("-"*40)

print("Total Marks:",total_marks)
print("Average Marks:",average)

Maximum_Possible_Marks=100*5
print("Maximum marks",Maximum_Possible_Marks)

#to print percentage
percentage=total_marks/Maximum_Possible_Marks*100
print("Percentage:",percentage)
