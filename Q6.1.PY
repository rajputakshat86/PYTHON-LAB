n = int(input())
nums = list(map(int, input().split()))
max_num = nums[0]
min_num = nums[0]
for num in nums[1:]:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
print(max_num, min_num)