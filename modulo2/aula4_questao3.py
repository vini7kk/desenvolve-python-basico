#3 - Você está desenvolvendo um programa para calcular o preço total de uma compra em uma loja online. O preço dos produtos é calculado 
# multiplicando a quantidade pelo preço unitário. Escreva um programa em Python que solicite do usuário o nome, o preço unitário e a 
# quantidade de 3 produtos comprados e imprima ao final o preço total da compra

#entrada de dados 
produto1 = str(input("qual o nome do produto?"))
valor_produto1 = float(input("qual o valor deste produto?"))
quantidade1 = int(input("qual a quantidade deste produto?"))

produto2 = str(input("qual o nome do produto?"))
valor_produto2 = float(input("qual o valor deste produto?"))
quantidade2 = int(input("qual a quantidade deste produto?"))

produto3 = str(input("qual o nome do produto?"))
valor_produto3 = float(input("qual o valor deste produto?"))
quantidade3= int(input("qual a quantidade deste produto?"))

#processamento

valor1 = valor_produto1 * quantidade1
valor2 = valor_produto2 * quantidade2   
valor3 = valor_produto3 * quantidade3
valor_total = valor1 + valor2 + valor3

#saida de dados

print("resumo da compra")
print(f"item: {produto1} preço: {valor_produto1} quantidade: {quantidade1}")
print(f"item: {produto2} preço: {valor_produto2} quantidade: {quantidade2}")
print(f"item: {produto3} preço: {valor_produto3} quantidade: {quantidade3}")
print(f"o valor total da compra é de {valor_total} reais.")