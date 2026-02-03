n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
