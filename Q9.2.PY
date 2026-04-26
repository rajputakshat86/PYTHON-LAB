class Student:
    def __init__(self, name, sap_id, phy, chem, maths):
        self.name = name
        self.sap_id = sap_id
        self.phy = phy
        self.chem = chem
        self.maths = maths

    def display(self):
        print("Name:", self.name)
        print("SAP ID:", self.sap_id)
        print("Physics:", self.phy)
        print("Chemistry:", self.chem)
        print("Maths:", self.maths)

    def marks_percentage(self):
        total = self.phy + self.chem + self.maths
        return (total / 300) * 100

    def result(self):
        if self.phy > 40 and self.chem > 40 and self.maths > 40:
            return "Pass"
        else:
            return "Fail"


def class_average(students):
    total_percent = 0
    for s in students:
        total_percent += s.marks_percentage()
    return total_percent / len(students)


students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    sap_id = input("Enter SAP ID: ")
    phy = int(input("Enter Physics marks: "))
    chem = int(input("Enter Chemistry marks: "))
    maths = int(input("Enter Maths marks: "))

    students.append(Student(name, sap_id, phy, chem, maths))

print("\nStudent Details:\n")

for s in students:
    s.display()
    print("Percentage:", s.marks_percentage())
    print("Result:", s.result())
    print("----------------------")

print("Class Average:", class_average(students))