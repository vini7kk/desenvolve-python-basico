#Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo. Anagramas são palavras com os mesmos caracteres
# rearranjados.

        #Digite uma frase: Meu amor mora em Roma e me deu um ramo de flores
        #Digite a palavra objetivo: amor
        # Anagramas: ["amor", "mora", "ramo", "Roma"] 

from itertools import permutations
#entrada de dados 
frase = str(input("Digite uma frase: ")).lower()
palavra_objetivo = str(input("Qual a palavra objetivo? ")).lower()

palavras = frase.split(" ") #separa as palavras através do " " espaço entre elas
anagramas_objetivo = set(''.join(p) for p in permutations(palavra_objetivo))
for palavra in palavras:
    if palavra in anagramas_objetivo:
        print(f"'{palavra}' é um anagrama de '{palavra_objetivo}'")
