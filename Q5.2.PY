n = int(input("Enter number of values: "))
values = tuple(int(input()) for _ in range(n))
average = sum(values) / n
print("Average =", average)
