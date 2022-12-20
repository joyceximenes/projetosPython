print("Bem vindo ao quiz da Copa 2022, se iniciará agora.")
start = input("Quer começar? (S/N) \n")
if start == "N":
    quit()

pontos = 0

print("                  QUIZ INICIADO!                \n")
print("Quem venceu a copa do mundo de 2022? \n A) França \n B) Croácia \n C) Argentina \n D) Brasil \n ")
pgt1 = input("Resposta:... \n")
if pgt1 == "C":
    print("Resposta correta!\n")
    pontos = pontos + 1
else: 
    print("Resposta errada\n")

print("Quem foi o artilheiro da copa do mundo de 2022? \n A) Neymar \n B) Mbappe \n C) Harry Kane \n D) Messi \n ")
pgt2 = input("Resposta:... \n")
if pgt2 == "B":
    print("Resposta correta!\n")
    pontos = pontos + 1
else: 
    print("Resposta errada\n")

print("Qual clube mais cedeu jogadores? \n A) Bayer \n B) Real Madrid \n C) Chelsea \n D) PSG \n ")
pgt3 = input("Resposta:... \n")
if pgt3 == "A":
    print("Resposta correta!\n")
    pontos = pontos + 1
else: 
    print("Resposta errada\n")

print(f"Chegamos ao final. Sua pontuação foi: {pontos} pontos")
