n = int(input("Enter number of movies: "))
movies = {}

for _ in range(n):
    name = input("Enter movie name: ")
    year = int(input("Enter release year: "))
    director = input("Enter director name: ")
    cost = float(input("Enter production cost: "))
    collection = float(input("Enter collection earned: "))
    movies[name] = {"year": year, "director": director, "cost": cost, "collection": collection}

print("\nAll movie details:")
for name, details in movies.items():
    print(name, ":", details)

print("\nMovies released before 2015:")
for name, details in movies.items():
    if details["year"] < 2015:
        print(name)

print("\nMovies that made a profit:")
for name, details in movies.items():
    if details["collection"] > details["cost"]:
        print(name)

director_name = input("\nEnter director name to search movies: ")
print(f"Movies directed by {director_name}:")
for name, details in movies.items():
    if details["director"] == director_name:
        print(name)
