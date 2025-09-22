#Juliana e Cris querem entrar em um bar, mas só podem se ambos forem maiores de idade (>17). Escreva um programa que solicite as idades de
#Juliana e Cris e imprima True se ambas forem maiores de 17 anos, indicando que podem entrar no bar, e False caso contrário.

#entrada de dados
idade_cris = int(input ("qual a idade da Cris?"))
idade_juliana = int(input ("qual a idade da Juliana?"))

#processamento
pode_entrar = idade_cris > 17 and idade_juliana > 17  



#saida de dados
print(pode_entrar)