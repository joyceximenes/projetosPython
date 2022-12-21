import random
import string

def gerador_senha (tam_senha = 8): #define 8 como padrão
    alfa_opcoes = string.ascii_letters # dá opções de letras
    num_opcoes = string.digits # dá opções de numeros
    pontu_opcoes = string.punctuation # dá opções de caracteres
    options = alfa_opcoes + num_opcoes + pontu_opcoes

    senha = ""
    for i in range(0, tam_senha):
        digito = random.choice(options)
        senha = senha + digito # agrega os caracteres

    return(senha)

resposta = gerador_senha()
print("senha gerada: " + resposta)
