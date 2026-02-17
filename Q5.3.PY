n = int(input("Enter number of students: "))
scores = [int(input()) for _ in range(n)]
unique_scores = list(set(scores))
unique_scores.sort()
runner_up = unique_scores[-2]
print(runner_up)
