#Preencha duas listas (lista1, lista2) com 20 valores inteiros aleatórios entre 0 a 50. Crie uma terceira lista interseccao contendo apenas os valores que se repetem nas duas listas. Ao final imprima:
    #-Ambas as listas
    #-A lista intersecção ordenada
    #-A quantidade de vezes que cada elemento aparece em cada lista
    #-Atenção, a lista de intersecções não pode ter duplicatas. 

#bibliotecas utilizadas:
import random
from collections import Counter

#criação das listas
lista1 = []
lista2 = []
lista3 = []

#preenchendo as listas com valores aleatorios
for _ in range(20) :
    num = random.randint(20,50)
    lista1.append(num)

for _ in range(20) :
    num = random.randint(20,50)
    lista2.append(num)

#criando uma terceira lista com a interseção da lista 1 e 2 / ordenando a 3 lista de forma crescente.
lista3 = list(set(lista1) & set(lista2)) 
lista3_ordenada = sorted(lista3)

#utilizando funções da biblioteca "collections" para contabilizar quantas vezes um número aparece em cada lista
contador1 = dict(Counter(lista1))
contador2 = dict(Counter(lista2))

#imprimindo os resultados
print("lista 1:", lista1)
print("\nlista 2:", lista2)
print("\nlista com os valores que aparecem nas listas 1 e 2 simultaneamente, em ordem crescente:", lista3_ordenada)

#para mostrar a contagem de cada número por vez (melhor visualização)
print("\nContagem na lista 1:")
for valor, qtd in contador1.items():
    print(f"{valor} aparece {qtd} vezes")

print("\nContagem na lista 2:")
for valor, qtd in contador2.items():
    print(f"{valor} aparece {qtd} vezes")
