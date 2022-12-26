# pegue duas listas e escreva um programa que retorne uma lista que contenha apenas os elementos comuns entre as listas
import random

l1 = random.sample(range(10), 6) # lista aleatoria
l2 = random.sample(range(10), 8)
print(l1)
print(l2)

com = []

for i in l1:
    if i in l2:
        com.append(i)
print(com)
