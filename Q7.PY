import math

a = 5
b = 6
c = 7

s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(area)
