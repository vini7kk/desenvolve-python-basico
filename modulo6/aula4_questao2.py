#Solicite uma frase do usuário e usando compreensão de listas imprima:
    #A lista de vogais da frase, ordenada alfabeticamente
    #A lista de consoantes da frase (remova espaços em branco)

frase = input("Digite uma frase: ").lower()
vogais = sorted([letra for letra in frase if letra in "aeiou"])
print(vogais)
consoantes = [letra for letra in frase if letra.isalpha() and letra not in "aeiou"]
print(consoantes)



