#Implemente um código que leia uma string do usuário e imprima quantas vogais existem na frase e quais os seus índices da string. 
# Dica: letra in "aeiou". Exemplo:

    #Digite uma frase: Meu amor mora em Roma e me deu um ramo de flores
    #19 vogais
    #Índices [1, 2, 4, 6, 10, 12, 14, 18, 20, 22, 25, 28, 29, 31, 35, 37, 40, 44, 46]

frase = str(input("digite uma frase: "))
vogais = ["a","e","i","o","u","A","E","I","O","U"]

quantidade = len(list(filter(lambda letra: letra in vogais, frase)))
indices_vogais = [i for i, l in enumerate(frase) if l in vogais]

print(quantidade)
print(indices_vogais)