#Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (com pelo menos 4 valores), os armazena
# em uma lista e, usando fatiamento de listas, imprima:

#A lista original;
#Os 3 primeiros elemento;
#Os 2 últimos elementos;
#A lista invertida (do fim para o começo);
#Os elementos de índice par (0, 2, 4 … );
#Os elementos de índice ímpar (1, 3, 5, … );

# criando a lista
lista = []

# pedindo ao usuário inserir os 4 elementos obrigatórios
for _ in range(4):
    num = int(input("Adicione um número à lista: "))
    lista.append(num)

# oferecendo ao usuário adicionar mais elementos
while True:
    resposta = input('Deseja adicionar mais elementos? responda com "sim" ou "não": ').lower()
    if resposta == "sim":
        num = input('Adicione um número à lista ou digite "sair" para parar: ').lower()
        if num == "sair":
            break
        if num.isdigit():
            lista.append(int(num))
        else:
            print("Valor inválido! Digite um número ou 'sair'.")
    elif resposta in ["não", "nao"]:
        break
    else:
        print('Resposta inválida! Digite apenas "sim" ou "não".')

# processando as informações da lista
invertida = lista[::-1]  # lista invertida
pares = lista[::2]       # elementos de índices pares
impares = lista[1::2]    # elementos de índices ímpares

# impressão dos dados
print(f"\nLista original: {lista}")
print("os 3 primeiros elementos:", lista[:3])
print("os 2 últimos elementos:", lista[-2:])
print("Lista invertida:", invertida)
print("Elementos em índices pares:", pares)
print("Elementos em índices ímpares:", impares)
print("\n")