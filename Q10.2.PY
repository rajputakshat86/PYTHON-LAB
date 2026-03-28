import numpy as np

arr = np.array([[5, 12, 7],
                [9, 3, 15],
                [6, 8, 10]])

sum_rows = np.sum(arr, axis=1)
sum_columns = np.sum(arr, axis=0)
second_max = np.sort(arr.flatten())[-2]

print("Array:")
print(arr)
print("Sum of each row:", sum_rows)
print("Sum of each column:", sum_columns)
print("Second maximum element:", second_max)