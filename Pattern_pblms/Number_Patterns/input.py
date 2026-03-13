name = input("Enter your name: ")
print(name)

# 
name = input("Enter student name: ")
roll = int(input("Enter roll number: "))
marks = float(input("Enter marks: "))

print(name, roll, marks)

#
n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    roll = int(input("Enter roll number: "))
    marks = float(input("Enter marks: "))

    print("Student Details:", name, roll, marks)