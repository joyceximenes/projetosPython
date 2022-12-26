# Escreva um programa (função!) que recebe uma lista e retorna uma nova lista que contém todos os elementos da primeira lista menos todas as duplicatas.

a = ["a", "ca", "dr", "ef"]
b = ["re", "dr", "ef", "wq"]
c = []
def func1(a, b):
    for i in a:
        if i not in b:
            c.append(i)
    for i in b:
        if i not in a:
            c.append(i)
    return c

z = func1(a, b)
print (z)
