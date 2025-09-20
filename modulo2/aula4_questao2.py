# Leia um valor inteiro correspondente a uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. 

#entrada de dados
F = int(input("Qual a temperatura em Fahrenheit? "))

#processamento
C = (F - 32) * (5/9)

#saida de dados
print(f"A temperatura em Celsius é {C:.2f}°C")