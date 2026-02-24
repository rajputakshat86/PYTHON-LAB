nums = list(map(int, input().split()))
max_min = lambda lst: (max(lst), min(lst))
print(max_min(nums))