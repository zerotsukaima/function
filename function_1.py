#def summa(*jd):
    #s = 0
    #for i in jd:
        #s = s + i
    #return s

#print(summa(1,2,3,))

x = 99

def func(y):
    #по хорошему не надо менять внутри функции глобальные переменные
    global x
    z = x + y
    x = 22
    return z

print(x)
print(func(1))
print(x)