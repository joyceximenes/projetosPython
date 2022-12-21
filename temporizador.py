import time

t = input("Digite o tempo em segundos: ")

if t.isdigit():
    t = int(t)
else:
    quit()



while t:
    minutos, segundos = divmod(t, 60) #divide o t por 60, para dar os minutos
    # o quociente e o resto
    timer = "{:02d}:{:02d}".format(minutos, segundos)
    print(timer, end="\r") # um print sobrescreve outro
    time.sleep(1)
    t = t - 1


