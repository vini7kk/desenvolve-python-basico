#Desenvolva um programa em Python que peça ao usuário para inserir dois números decimais e calcule a diferença absoluta entre esses dois 
#números. Utilize a função nativa abs para garantir que o resultado seja sempre positivo e round para arredondar o resultado para duas 
#casas decimais.

#entrada de dados
num1 = float(input("digite um número com casas decimais: "))
num2 = float(input("digite um número com casas decimais: "))

#processamento:
diferenca = abs(num1 - num2)
diferenca = round(diferenca, 2)  # arredonda para 2 casas decimais

#saida de dados
print(f"a diferença entre {num1:.2f} e {num2:.2f} é de : {diferenca:.2f}")
