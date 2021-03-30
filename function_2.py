def a(n):
    if n == 1:
        print(1)
    else:
        b = n - a * (a * (n - 1))

n = int(input("Введите число "))
print(a(n))