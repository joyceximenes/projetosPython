# Digamos que eu lhe dê uma lista salva em uma variável: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Escreva uma linha de Python que pegue essa lista e crie uma nova lista que tenha apenas os elementos pares dessa lista.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
par = []

for i in a:
    if i % 2 == 0:
        par.append(i)
print(par)
