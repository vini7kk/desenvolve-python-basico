#Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.


from num2words import num2words #biblioteca que já possui função de converter número para número por extenso

Lista_mes = ["0", "janeiro", "fevereiro", "março", "abril", "maio", 
             "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

# Entrada do usuário com loop em caso de dados errados
while True:
    data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa) ou 0 para sair: ")
    
    if data_nascimento == "0":
        print("Programa encerrado.")
        exit()  # sai do programa imediatamente
    
    if len(data_nascimento) == 10 and data_nascimento[2] == '/' and data_nascimento[5] == '/':
        break
    
    print("Formato inválido! Tente novamente (ex: 05/03/2002)")
    
# Separar dia, mês e ano
data_separada = data_nascimento.split("/")
dia = int(data_separada[0])
mes = int(data_separada[1])
ano = int(data_separada[2])
12
#converter para extenso usando num2words
dia_extenso = num2words(dia, lang='pt')
ano_extenso = num2words(ano, lang='pt')

#convertendo mês inserido pelo usuario, para seu nome
mes_nome = Lista_mes[mes]

# Exibir resultado
print(f"Você nasceu em {dia_extenso} de {mes_nome} de {ano_extenso}.")