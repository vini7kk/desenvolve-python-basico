# Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de valores.
# Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. 
# Intercale os elementos até o final da primeira lista, adicionando ao final os elementos remanescentes da maior lista.

lista1 = []
lista2 = []
lista_combinada = []

num = int(input(f"digite a quantidade de elementos da lista 1:"))
for _ in range (num):
    resposta = int(input("insira um valor para a lista:" ))
    lista1.append(resposta)
num = int(input(f"digite a quantidade de elementos da lista 2:"))
for _ in range (num):
    resposta = int(input("insira um valor para a lista:" ))
    lista2.append(resposta)

min_len = min(len(lista1), len(lista2))

# intercalando até o final da menor lista
for i in range(min_len):
    lista_combinada.append(lista1[i])
    lista_combinada.append(lista2[i])

# adicionando elementos restantes da lista maior
lista_combinada.extend(lista1[min_len:])
lista_combinada.extend(lista2[min_len:])

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista combinada:", lista_combinada)