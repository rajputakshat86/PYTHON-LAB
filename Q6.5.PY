import math

r, h = map(float, input().split())
volume = lambda r, h: (1/3) * math.pi * r**2 * h
print(volume(r, h))