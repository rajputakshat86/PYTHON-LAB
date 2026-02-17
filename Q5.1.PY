n = int(input("Enter number of values: "))
counts = [0, 0, 0, 0]

for _ in range(n):
    value = int(input())
    if 0 <= value <= 3:
        counts[value] += 1

for i in range(4):
    print(f"{i} occurred {counts[i]} times")
