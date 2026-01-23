import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

D = b**2 - 4*a*c  # Discriminant

if D > 0:
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)
    print("Roots are real and different:", root1, root2)
elif D == 0:
    root = -b / (2*a)
    print("Roots are real and equal:", root)
else:
    realPart = -b / (2*a)
    imagPart = math.sqrt(-D) / (2*a)
    print("Roots are imaginary:", f"{realPart}+{imagPart}i", f"{realPart}-{imagPart}i")
