n = int(input("Enter number of fruits in each set: "))

s1 = set()
s2 = set()

print("Enter fruits for set s1:")
for i in range(n):
    s1.add(input())

print("Enter fruits for set s2:")
for i in range(n):
    s2.add(input())

print("Fruits in both s1 and s2:", s1 & s2)
print("Fruits only in s1 but not in s2:", s1 - s2)
print("Count of all fruits from s1 and s2:", len(s1 | s2))
