#1 - Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura), bem como o preço do metro quadrado da região em ponto flutuante. Calcule o valor do terreno e imprima o resultado como mostra o exemplo a seguir:


#entrada dos dados
largura = float(input("Qual a largura do terreno? "))
comprimento = float(input("Qual o comprimento do terreno? "))
valor_por_metro = float(input("Qual o valor por m² na região? "))

#processamento
valor_do_terreno = largura * comprimento * valor_por_metro

#saida de dados
print(f"o valor do terreno é de {valor_do_terreno:.2f} reais. ")