#Escreva um código que gere n valores inteiros aleatórios entre 0 e 100 e calcule a raíz quadrada da soma dos valores. 
# Peça ao usuário o valor de n

import math
import random
#entrada de dados
quantidade = int(input("diga-me a quantidade de valores inteiros aleatórios entre 0 e 100 que irei gerar e calcular a raíz quadrada da soma dos valores: "))

#processament
soma = 0
for _ in range(quantidade):
    numero = random.randint(0,100)
    print(f"número gerado: {numero}")
    soma += numero

raiz = math.sqrt(soma)
 
 #saida:
print(f"A soma dos valores gerados foi {soma} e a raíz quadrada dessa soma é {raiz:.2f}")

