# programa que lê o nome e a idade e informa em que ano o usuário fará 100 anos
nome = input("Qual seu nome? \n")

idd = input("Informe sua idade: ")
idd = int(idd)

ano = 2022 + 100 - idd

print(f"{nome}, você fará 100 anos em {ano}")
