#Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente. Em seguida encontre o intervalo que possui a maior quantidade de
# números negativos e delete ele da lista com o operador del. Você deve imprimir a lista antes e depois da deleção.

import random

# Gerar a lista
lista = [random.randint(-10, 10) for _ in range(20)]
print("Lista original:\n", lista)

# Inicializar variáveis para encontrar o maior trecho negativo
max_negativos = 0
inicio_max = 0
fim_max = 0

#  Percorrer a lista para encontrar o maior trecho consecutivo de negativos
i = 0
while i < len(lista):
    if lista[i] < 0:
        inicio = i
        count = 0
        # contar sequência de negativos
        while i < len(lista) and lista[i] < 0:
            count += 1
            i += 1
        fim = i
        if count > max_negativos:
            max_negativos = count
            inicio_max = inicio
            fim_max = fim
    else:
        i += 1

#  Deletar o trecho com mais números negativos
if max_negativos > 0:
    del lista[inicio_max:fim_max]

print("\nLista após remover o maior trecho de números negativos:\n", lista)