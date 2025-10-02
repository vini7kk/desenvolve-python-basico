#Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista. Em seguida imprima na ordem estabelecida:

#A lista ordenada, sem modificar a lista original

#A lista original

#O índice do maior valor da lista

#O índice do menor valor da lista


import random

#criação da lista
lista = []
for _ in range (20): #para cada repetição faça: (repete 20x)
    num = random.randint(-100,100)
    lista.append(num)

ordenada = sorted(lista) #separar a lista original da ordenada

#saida dos dados
print (f"lista ordenada:", ordenada) 
print (f"lista original:", lista)
print (f"o maior valor da lista:", lista.index(max(lista))) #imprima o indice de maior valor dentro da lista
print (f"o menor valor da lista:", lista.index(min(lista))) #imprima o indice de menor valor dentro da lista