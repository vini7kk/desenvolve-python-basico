#umm instituto realizou uma pesquisa de público e precisa calcular a média de idade dos respondentes. Escreva um programa que leia um 
# inteiro N com a quantidade de respondentes e em seguida leia as N idades de cada respondente. Ao final, imprima a média das idades.

#entrada de dados

N = int(input("qual o número de respondentes? "))
cont = 0
idade_total = 0
media = 0
#processamento

while  cont < N:

    idade = int(input("Digite a idade dos respondentes: "))
    idade_total += idade
    cont += 1

    media = idade_total / N

#saida de dados
print(f"a media de idade do seu publico respondentes é de :{media:.0f} anos.")