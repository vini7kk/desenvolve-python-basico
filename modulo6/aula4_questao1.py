#Escreva um script python que use compreensão de listas para criar as seguintes listas:
    #Todos os números pares entre 20 e 50, ou seja, [20, 22, 24, …, 48, 50]
    #Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]
    #Todos os números entre 1 e 100 que sejam divisíveis por 7
    #Para todos os valores em range(0,30,3), escreva "par" ou "ímpar" dependendo da paridade do elemento (ex:['par', 'impar',… , 'impar']) 


lista = [num for num in range(20, 51, 2)] #Para cada num que vai de 20 até 50, de 2 em 2, coloque num dentro de uma lista chamada lista.
print (lista)

quadrado_lista = [num**2 for num in lista]
print(quadrado_lista)

lista2 = [num for num  in range(0,101,7) if num % 7 == 0]
print(lista2)

lista3 = ["par" if num % 2 == 0 else "impar" for num in range (0,30,3)]
print(lista3)