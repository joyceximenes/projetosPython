# Escreva um programa que receba uma lista de números (por exemplo, a = [5, 10, 15, 20, 25]) e crie uma nova lista apenas com o primeiro e o último elementos da lista fornecida. Para praticar, escreva este código dentro de uma função.

a = [5, 10, 15, 20, 25]
l = []

def pu(a):
    return (a[0], a[len(a)-1])
    
l = pu(a)
print(l)
