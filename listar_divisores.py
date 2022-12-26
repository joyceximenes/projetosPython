# Crie um programa que peça ao usuário um número e imprima uma lista de todos os divisores desse número. 

n = input("Informe um número: ")
n = int(n)
div = []

x = list(range(1, n + 1)) # faz uma lista de 1 a n+1

for num in x:
    if n % num == 0:
        div.append(num)

print(div)
