#Crie a função encrypt() que recebe uma lista de strings e retorna os nomes criptografados, bem como a chave da criptografia. Regras:

# Chave de criptografia: gere um valor n aleatório entre 1 e 10

# Substitua cada caracter c pelo caracter c + n. Trabalharemos apenas com o intervalo de caracteres visíveis 
# (entre 33 e 126 na tabela Unicode)
  
import random

lista_nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

def encrypt(lista):
    # Gera a chave aleatória entre 1 e 10
    n = random.randint(1,10)
    
    # Lista para guardar os nomes criptografados
    lista_criptografada = []
    
    # Percorre cada nome da lista
    for nome in lista:
        nome_criptografado = ""
        # Percorre cada letra do nome
        for letra in nome:
            codigo = ord(letra)          # código Unicode da letra
            novo_codigo = codigo + n     # aplica a chave
            # garante que o caractere fique entre 33 e 126
            novo_codigo = 33 + (novo_codigo - 33) % (126 - 33 + 1)
            novo_letra = chr(novo_codigo)  # transforma de volta em caractere
            nome_criptografado += novo_letra
        # adiciona o nome criptografado à lista
        lista_criptografada.append(nome_criptografado)
    
    # retorna a lista criptografada e a chave
    return lista_criptografada, n

# Testando a função
nomes_criptografados, chave = encrypt(lista_nomes)
print("Chave:", chave)
print("Nomes criptografados:", nomes_criptografados)