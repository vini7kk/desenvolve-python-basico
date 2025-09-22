# Dando continuidade à questão anterior, um outro bar permite a entrada de grupos onde pelo menos uma pessoa é maior de idade (ficando 
# responsável pelas outras). Ajuste sua resposta da questão anterior, ainda solicitando as idades de Juliana e Cris, mas ajustando a 
# expressão para esse novo cenário, imprimindo True se puderem entrar no bar, e False caso contrário.

#entrada de dados
idade_cris = int(input ("qual a idade da Cris?"))
idade_juliana = int(input ("qual a idade da Juliana?"))

#processamento
if idade_cris > 17 or idade_juliana > 17 :
    pode_entrar =  True
else :
    pode_entrar = False

#poderia ser usado apenas: pode_entrar = idade_cris > 17 or idade_juliana > 17 , mas quis já por em pratica o se e senão.

#saida de dados
print(pode_entrar)


