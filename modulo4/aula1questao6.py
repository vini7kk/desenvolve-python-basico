#Maria precisa de sua ajuda para organizar os experimentos de seu laboratório. Ela quer saber quantas cobaias foram utilizadas no 
# laboratório e o percentual de cada tipo de cobaia utilizada. Este laboratório utiliza três tipos de cobaias: sapos, ratos e coelhos. 

#Entrada: A primeira linha de entrada é um inteiro N com a quantidade de experimentos registrados. As N linhas seguintes contém um inteiro 
# Quantia que representa a quantidade de cobaias utilizadas e um caractere Tipo ('S', 'R' ou 'C') com o tipo de cobaia (S:Sapo, R:Rato ou C:Coelho).

#Saída: Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia e o percentual de cada uma em relação ao total de cobaias utilizadas


#entrada
# Entrada do número de experimentos
N = int(input("Quantos experimentos foram registrados? "))

# Inicializa contadores
S = 0  # sapos
R = 0  # ratos
C = 0  # coelhos

# Loop para registrar cada experimento
for i in range(N):
    quantidade, tipo = input(f"Experimento {i+1}: ").split()
    quantidade = int(quantidade)
    tipo = tipo.upper()
    
    if tipo == 'S':
        S += quantidade
    elif tipo == 'R':
        R += quantidade
    elif tipo == 'C':
        C += quantidade

# Processamento
total = S + R + C
percentual_S = (S / total) * 100
percentual_R = (R / total) * 100
percentual_C = (C / total) * 100

# Saída de dados
print(f"Total de cobaias: {total}")
print(f"Total de sapos: {S}")
print(f"Total de ratos: {R}")
print(f"Total de coelhos: {C}")
print(f"Percentual de sapos: {percentual_S:.2f}%")
print(f"Percentual de ratos: {percentual_R:.2f}%")
print(f"Percentual de coelhos: {percentual_C:.2f}%")
