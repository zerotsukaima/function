def a(n):
    if n == 1:
        return 1
    else:
        y = n - a(a(n - 1))
        return y

for i in range(1, 10):
    print(a(i), end=' ')