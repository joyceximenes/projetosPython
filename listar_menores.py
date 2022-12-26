# pegue uma lista e escreva um programa que imprima todos os elementos da lista menores que 5.

l = [2, 8, 34, 80, 0 , -6]
x = []
for i in l:
    if i < 5:
        x.append(i) # adiciona em uma nova lista
print(x)        
