n = int(input())

def fibonacci_series(a, b, count, n):
    if count == n:
        return
    print(a, end=' ')
    fibonacci_series(b, a + b, count + 1, n)

fibonacci_series(0, 1, 0, n)