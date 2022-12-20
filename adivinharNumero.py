import random

print("Ola, este é um adivinhador de número")
nummax = input("Para começar, digite o maior número desejado: ")

if nummax.isdigit():
    nummax = int(nummax)
else:
    quit()

#gerando o numero randomico
randomnum = random.randint(0, nummax)

while True:
    resposta = input("Adivinhe o número..")
    if resposta.isdigit():
        resposta = int(resposta)
    else:
        print("Informe um número.")
        continue

    if resposta == randomnum:
        print("Acertou")
        break 
    elif resposta > randomnum:
        print("O número informado está acima do gerado")
    else:
        print("O número informado está abaixo do gerado")
    