#Faça um programa que leia um número de celular e, caso o número tenha apenas 8 dígitos, acrescente o 9 na frente. Caso o número já tenha 
# 9 dígitos, verifique se o primeiro dígito é 9. Adicione o separador "-" na sua impressão.

DDD = str(input("digite o seu DDD: "))
while True:
    num = str(input("digite seu número e irei formata-lo: "))
    quantidade = len(num)
    if quantidade == 8:
        num = "9" + num
        break
    elif quantidade == 9 and num[0] == "9":  
        break
    else:
        print("o número informado não existe. tente novamente.")

numero_formatado = (num[:5] + "-") + num[5:]
print(f"o seu número é: ({DDD}) {numero_formatado}")
