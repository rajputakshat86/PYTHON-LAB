try:
    with open("counter.txt", "r") as f:
        count = int(f.read().strip())
except FileNotFoundError:
    count = 0

count += 1
print("This program has been executed", count, "times.")

with open("counter.txt", "w") as f:
    f.write(str(count))