student={
  "name":"Hema",                     #dictionary
  "age":18,
  "skill":"python"
}
print(student)
print(student["skill"])     #accessing
student["college"]="Aditya degree college"#add a new item
print(student)
student["age"]=19 #changing value
print(student)
student.pop("age")
print(student)
print(len(student)) #length of dictionary
print(student.keys()) #get only key
print(student.values()) #get only values
print(student.items()) #get key-value pairs
