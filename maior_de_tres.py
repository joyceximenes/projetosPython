# Implemente uma função que recebe como entrada três variáveis ​​e retorna a maior das três.


a = input("Informe a variavel ")
b = input("Informe a variavel ")
c = input("Informe a variavel ")
a = int(a)
b = int(b)
c = int(c)



def max(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c > a and c > b:
        return c
z = max(a,b,c)
print(f"a maior variável informada é {z}")
