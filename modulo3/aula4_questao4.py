#Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso do pacote. Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:

#Distância até 100 km: R$1 por kg.
#Distância entre 101 e 300 km: R$1.50 por kg.
#Distância acima de 300 km: R$2 por kg.
#Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg

# entrada de dados 
peso = float(input("Qual o peso da encomenda em Kg? "))
distancia = float(input("Qual a distância em KM da entrega? "))

# processamento
if distancia <= 100:
    custo = peso * 1
elif 100 < distancia <= 300:
    custo = peso * 1.5
else:  # acima de 300
    custo = peso * 2

# acrescentar taxa se o peso for maior que 10kg
if peso > 10:
    custo += 10

# saída de dados
print(f"O valor do frete é R${custo:.2f}")