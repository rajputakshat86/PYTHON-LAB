try:
    with open("city.txt", "r") as f:
        cities = [line.strip().split() for line in f.readlines()]
except FileNotFoundError:
    with open("city.txt", "w") as f:
        f.write("Dehradun 5.78 308.20\nDelhi 190 1484\nMumbai 204 603\nKolkata 149 205\nChennai 88 426\n")
    with open("city.txt", "r") as f:
        cities = [line.strip().split() for line in f.readlines()]

for city in cities:
    print("City:", city[0], "Population:", city[1], "Area:", city[2])

print("\nCities with population > 10 Lakhs:")
for city in cities:
    if float(city[1]) > 10:
        print(city[0])

total_area = sum(float(city[2]) for city in cities)
print("\nSum of areas of all cities:", total_area)