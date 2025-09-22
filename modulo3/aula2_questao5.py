#Solicite de um usuário seu gênero ("M" ou "F"), sua idade e seu tempo de serviço (em anos) e escreva uma expressão que imprima True se
#a pessoa já pode se aposentar, ou False caso contrário, de acordo com as seguintes regras:

#A: Para mulheres, ter mais de 60 anos. Para homens, 65.

#B: Ou ter trabalhado pelo menos 30 anos

#C: Ou ter 60 anos  e trabalhado pelo menos 25.


#entrada de dados

genero = input("qual seu genero? (use M para Homem e F para mulher): ").strip().upper()
idade = int(input("qual sua idade? "))
tempo = int(input("quantos anos de serviço? "))

# processamento
if (genero == 'M' and idade > 64) or (genero == 'F' and idade > 59) or (tempo > 29) or (idade > 59 and tempo > 24):
    aposentadoria = True
else:
    aposentadoria = False   

# saída de dados 
print(aposentadoria)