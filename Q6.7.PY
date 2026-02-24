def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

name = input()
age = int(input())
greet(age=age, name=name)

def power(x, y=2):
    return x ** y

x = int(input())
y = input()
if y:
    y = int(y)
    print(power(x, y))
else:
    print(power(x))

def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

nums = list(map(int, input().split()))
print(sum_all(*nums))