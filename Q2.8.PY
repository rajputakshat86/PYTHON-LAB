name = input("Name: ")
roll = input("Roll Number: ")
sapid = input("SAPID: ")
sem = input("Sem: ")
course = input("Course: ")

subjects = ["PDS", "Python", "Chemistry", "English", "Physics"]
marks = []

for sub in subjects:
    marks.append(float(input(f"{sub}: ")))

total = sum(marks)
percentage = total / 5
cgpa = percentage / 10

if 0 <= cgpa <= 3.4:
    grade = "F"
elif 3.5 <= cgpa <= 5.0:
    grade = "C+"
elif 5.1 <= cgpa <= 6.0:
    grade = "B"
elif 6.1 <= cgpa <= 7.0:
    grade = "B+"
elif 7.1 <= cgpa <= 8.0:
    grade = "A"
elif 8.1 <= cgpa <= 9.0:
    grade = "A+"
elif 9.1 <= cgpa <= 10.0:
    grade = "O"

print(f"\nName: {name}")
print(f"Roll Number: {roll}   SAPID: {sapid}")
print(f"Sem: {sem}      Course: {course}\n")
for i in range(5):
    print(f"{subjects[i]}: {marks[i]}")
print(f"Percentage: {percentage}%")
print(f"CGPA: {cgpa}")
print(f"Grade: {grade}")
