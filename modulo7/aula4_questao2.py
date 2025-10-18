#Escreva um script que leia o arquivo salvo no exercício anterior e salva em um novo arquivo "palavras.txt",
#removendo todos os espaços em branco e caracteres não alfabéticos, e separando cada palavra em uma linha. Ao final, imprima o conteúdo do arquivo "palavras.txt".

palavras = []

# Abrir o arquivo original e ler o conteúdo
with open("frase.txt", "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()

# Separar o texto em palavras
lista_palavras = texto.split()

# Filtrar apenas caracteres alfabéticos
for p in lista_palavras:
    palavra_limpa = ''.join([c for c in p if c.isalpha()])  # mantém só letras
    if palavra_limpa:  # adiciona apenas palavras que não ficaram vazias
        palavras.append(palavra_limpa)

# Salvar o resultado em 'palavras.txt', uma palavra por linha
with open("palavras.txt", "w", encoding="utf-8") as arquivo_saida:
    for palavra in palavras:
        arquivo_saida.write(palavra + "\n")

# Imprimir o conteúdo do arquivo gerado
with open("palavras.txt", "r", encoding="utf-8") as arquivo_saida:
    print(arquivo_saida.read())