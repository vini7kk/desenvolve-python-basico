# entrada de dados
n = int(input("digite o valor de n: "))
maior = 0

# processamento
while n > 0:
    x = int(input("digite o valor de x: "))
    if x > maior:
        maior = x
    n = n - 1

# saída
print("Maior valor digitado:", maior)
