#Escreva um programa em Python que utiliza a biblioteca random para gerar um número aleatório entre 1 e 10 e peça ao usuário para adivinhar
#o número. Forneça feedback se o palpite é muito alto, muito baixo ou correto. Interrompa a execução somente quando o usuário acertar
#o palpite.


import random
#inicio
número = random.randint(1,10)
print("tente adivinhar um número entre 1 e 10. ")
resposta = int(input("digite um número entre 1-10: "))

while True:
    if resposta == número:
        print("você acertou!")
        break
    else:
        print("tente novamente...")
        if número < resposta:
            print("o palpite muito alto")
        else:
            print("palpite muito baixo")
        resposta = int(input("digite um número entre 1-10: "))