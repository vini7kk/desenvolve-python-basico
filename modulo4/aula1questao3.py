#processamento
n1 = int(input ("digite valor de n1: "))
n2 = int(input ("digite valor de n2: "))
n3 = int(input ("digite valor de n3: "))

#processamento

m = (n1 + n2 + n3) / 3

if m >=60:
    resultado ="aprovado"
elif m >= 40:
    resultado = "recuperação"
else:
    resultado = "Reprovado"

#saida de dados
print(resultado)
print("Fim")