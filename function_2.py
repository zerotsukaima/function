def a(n):
    if n == 1 or n == 0:
        return 1
    else:
        y = n - a(a(n - 1))
        return y

for i in range(0, 10):
    print(a(i), end=' ')