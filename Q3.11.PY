n = int(input("Enter the value of n: "))

sum_series = 0.0

for i in range(1, n + 1):
    sum_series += 1 / i

print("Sum of the series is:", sum_series)
