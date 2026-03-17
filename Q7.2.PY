try:
    with open("numbers.txt", "r") as f:
        numbers = [int(line.strip()) for line in f.readlines()]
except FileNotFoundError:
    with open("numbers.txt", "w") as f:
        f.write("50\n150\n200\n75\n120\n90\n")
    with open("numbers.txt", "r") as f:
        numbers = [int(line.strip()) for line in f.readlines()]

max_number = max(numbers)
average = sum(numbers)/len(numbers)
count_gt_100 = len([num for num in numbers if num > 100])

print("Maximum number:", max_number)
print("Average of numbers:", average)
print("Numbers greater than 100:", count_gt_100)