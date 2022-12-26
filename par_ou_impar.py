# Peça um número ao usuário. Dependendo se o número é par ou ímpar, imprima uma mensagem apropriada para o usuário. 
# Se o número for múltiplo de 4, imprima uma mensagem diferente.

n = input ("Informe um número: ")
n = int(n)
if n % 2 == 0:
    print("Numero par.\n")
else:
    print("Número ímpar.\n")
if n % 4 == 0:
    print("é um número divisível por 4")
