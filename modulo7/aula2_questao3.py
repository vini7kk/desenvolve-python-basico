import string 

while True:
    frase = input("Digite uma frase (ou 'Fim' para encerrar): ")
    
    if frase.lower() == "fim":
        print("Programa encerrado.")
        break
    
    # remover espaços, pontuação e colocar em minúsculas
    frase_normalizada = frase.lower()
    for char in string.punctuation + " ":
        frase_normalizada = frase_normalizada.replace(char, "")
    
    # Verificar se é palíndromo
    if frase_normalizada == frase_normalizada[::-1]:
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo.")