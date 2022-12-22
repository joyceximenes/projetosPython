import json
import random

f = open("words.json", encoding="utf8") # abrir arquivos

words = json.load(f) # traz o arquivo pra variavel
esco_pc = random.choice(list(words.keys())) # forcar que as chaves do json sejam listas

tent = 5
win = False

while tent > 0 and win is not True:
    print("Dica: " + words[esco_pc])
    resp = input("Olá, digite a data em formato DDMMAAAA: ")
    print("\n")
    if len(resp) != 8:
        print("Digite um formato de data válido")
        continue
    if resp.isdigit(): 
        check = []
        pont = 0
        for i in range(8): #i vai de 0 a 7
            if resp[i] == esco_pc[i]:
                check.append("✔️") # vai escrevendo na estrutura
                pont = pont + 1
            else:
                check.append("❌")
        print("Resposta: \n")
        print(" | ".join(check))
        print("  | ".join(resp))
        
        if pont == 8:
            win = True

    else: 
        print("Erro. Informe um número")
        continue

    tent = tent - 5
    

