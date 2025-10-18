#Escreva um script Python que solicita uma frase do usuário e a salve em um arquivo chamado "frase.txt" no mesmo local 
# do seu script. Imprima em seguida o caminho completo do arquivo salvo.


import os

# Solicita a frase do usuário
frase = input("Digite uma frase: ")

# Cria/sobrescreve o arquivo 'frase.txt' e grava a frase
with open("frase.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(frase)

# Obtém e exibe o caminho completo do arquivo
caminho = os.path.abspath("frase.txt")
print("Arquivo salvo em:", caminho)
