# Escreva uma função que receba uma lista de números e outro número. A função decide se o número fornecido está ou não dentro da lista e retorna um booleano apropriado.

import random
a = random.sample(range(10), 5)
n = input("Escolha o número: ")
n = int(n)
def pes(a, n):
    if n in a:
        return True
    else: 
        return False
z = pes(a,n)
print(z)
print(f"a lista fornecida foi: {a}")
