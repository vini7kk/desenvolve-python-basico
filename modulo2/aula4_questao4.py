#Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule a menor quantidade possível de notas necessárias
#para pagar aquele valor. As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. 


#entrada de dados
valor = int(input("qual valor do saque?"))
n1 = 100
n2 = 50
n3 = 20
n4 = 10
n5 = 5
n6 = 2
n7 = 1

#processamento

nts100 = valor // 100
valor = valor % 100

nts50 = valor // 50
valor = valor % 50

nts20 = valor // 20
valor = valor % 20

nts10 = valor // 10
valor = valor % 10

nts5 = valor // 5
valor = valor % 5

nts2 = valor // 2
valor = valor % 2

nts1 = valor // 1
valor = valor % 1

# Saída de dados
print(f"Notas de 100: {nts100}")
print(f"Notas de 50: {nts50}")
print(f"Notas de 20: {nts20}")
print(f"Notas de 10: {nts10}")
print(f"Notas de 5: {nts5}")
print(f"Notas de 2: {nts2}")
print(f"Notas de 1: {nts1}")