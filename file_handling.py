#creating a file
f=open("student.txt",'w')
f.write(" few students got again average marks.")
f.close()

#read a file
f=open("students.txt","r")
data=f.read()
print(data)
f.close()

#read line by line
f=open("students.txt","r")
for line in f:
  print(line, end="")
f.close()

#append data
f=open("students.txt","a")
f.write("one new line added by using append mode.")
f.close()

#instead of manual open/close, use with open()
with open("students.txt","r") as f:
  print(f.read())
