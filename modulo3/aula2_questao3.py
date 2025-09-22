#Você está desenvolvendo um sistema de admissão para um clube juvenil de jogos de tabuleiro. Escreva um programa em Python que pergunte ao 
# usuário sua idade, se já jogou pelo menos 3 jogos de tabuleiro (resposta deve ser True ou False) e quantas vezes venceu um jogo.
#  O programa deve imprimir True se o participante tiver entre 16 e 18 anos, já tiver jogado pelo menos 3 jogos e já ter vencido pelo 
# menos 1 jogo, permitindo seu ingresso no clube. Sua expressão deve imprimir False caso contrário.

#entrada de dados
idade = int (input("qual sua idade?"))
partidas = int (input("quantas partidas jogou?"))
venceu = int (input("qual o número de vitorias até o momento?"))

#processamento
if idade > 15 and idade < 18 :
    requisito1 = True
else :
    requisito1 = False


if partidas > 2:
    requisito2 = True
else :
    requisito2 = False

if venceu != 0 :
    requisito3 = True
else:
    requisito3 = False

if requisito1 and requisito2 and requisito3:
    qualificado = True
else:
    qualificado = False

#saida de dados 

print(qualificado)