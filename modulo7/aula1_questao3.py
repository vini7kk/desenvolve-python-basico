#Escreva um script que dado uma frase conta os espaços em branco.

    # Digite a frase: Meu amor mora em Roma e me deu um ramo de flores
    # Espaços em branco: 11

frase = str(input("Digite uma frase: "))

contador_de_espaço = int(frase.count(" ")) #contabiliza cada espaço entre as palavras dentro da frase

print(f"essa frase possui {contador_de_espaço} espaços.")