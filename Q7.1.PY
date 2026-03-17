try:
    with open("name.txt", "r") as f:
        names = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    with open("name.txt", "w") as f:
        f.write("Alice\nBob\nEve\nOscar\nUma\n")
    with open("name.txt", "r") as f:
        names = [line.strip() for line in f.readlines()]

total_names = len(names)
vowel_names = len([name for name in names if name[0].lower() in 'aeiou'])
longest_name = max(names, key=len)

print("Total names:", total_names)
print("Names starting with a vowel:", vowel_names)
print("Longest name:", longest_name)