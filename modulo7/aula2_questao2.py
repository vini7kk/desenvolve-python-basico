#Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".

#entrada de dados

frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
frase_sem_vogal = ""

for letra in frase:
    if letra in vogais:
        frase_sem_vogal += "*"
    else:
        frase_sem_vogal += letra

print(frase_sem_vogal)