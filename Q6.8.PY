n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    d[key] = int(value)

all_same = lambda dic: len(set(dic.values())) == 1
print(all_same(d))