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
        print("----------------------")

students = []

for i in range(3):
    name = input("Enter name: ")
    sap_id = input("Enter SAP ID: ")
    phy = int(input("Enter Physics marks: "))
    chem = int(input("Enter Chemistry marks: "))
    maths = int(input("Enter Maths marks: "))

    s = Student(name, sap_id, phy, chem, maths)
    students.append(s)

print("\nStudent Details:\n")

for s in students:
    s.display()