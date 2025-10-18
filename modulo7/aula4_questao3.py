#Baixe o arquivo contendo o roteiro do filme brasileiro "Estômago" e salve em seu computador com o nome "estomago.txt".
#  Em seguida crie um script em Python que abra o arquivo para leitura e imprima: 
    #O texto das primeiras 25 linhas

    #O número de linhas do arquivo

    #A linha com maior número de caracteres

    #O número de menções aos nomes dos personagens "Nonato" e "Íria" (inclua todas as variações de maiúsculas e
    #  minúsculas e atenção para não incluir a substring "iria" se ela fizer parte de outras palavras).

with open("estomago.txt", "r", encoding="UTF-8") as arquivo:
    texto = arquivo.read()  # Lê todo o conteúdo do arquivo

# Imprime as primeiras 25 linhas
linhas = texto.splitlines()  # Cria lista de linhas
print(''.join(linhas[:25]))

# Número de linhas
num_linhas = len(linhas)
print(f"Número total de linhas: {num_linhas}")

# Linha com maior número de caracteres
linha_maior = max(linhas, key=len)
print(f"Linha com maior número de caracteres:\n{linha_maior}")

# Número de menções aos personagens
palavras_do_texto = texto.split()  # Divide em palavras
nomes = ["nonato", "íria"]

numero_de_aparecoes = 0
for palavra in palavras_do_texto:
    if palavra.lower() in nomes:  # ignora maiúsculas/minúsculas
        numero_de_aparecoes += 1

print(f"Número de menções aos personagens: {numero_de_aparecoes}")
