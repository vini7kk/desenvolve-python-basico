# Desenvolva um validador de CPF. Solicite do usuário um CPF na forma XXX.XXX.XXX-XX (lido como string) 
# e imprima "Válido" ou "Inválido". 

cpf_validação = None

# função para validar primeiro dígito após "-" do CPF
def validação1(cpf):
    validados = []
    multiplicador = 10
    nove_digitos = cpf[:9]
    for n in nove_digitos:
        n = int(n)  # converte para número
        validados.append(n * multiplicador)
        multiplicador -= 1
    return sum(validados)


# função para validar o segundo dígito após "-" do CPF
def validação2(cpf_com_digito1):
    validados = []
    multiplicador = 11
    for n in cpf_com_digito1:
        n = int(n)
        validados.append(n * multiplicador)
        multiplicador -= 1
    return sum(validados)


# entrada de dados
cpf = str(input("Digite seu CPF (XXX.XXX.XXX-XX): "))

# <<< correção: remover pontos e traço para trabalhar apenas com números
cpf_limpo = cpf.replace(".", "").replace("-", "")

# processamento dos dados
validação_digito1 = validação1(cpf_limpo)

resto1 = validação_digito1 % 11
if resto1 < 2:
    digito1 = 0
else:
    digito1 = 11 - resto1

cpf_com_digito_1 = cpf_limpo[:9] + str(digito1)

validação_digito2 = validação2(cpf_com_digito_1)
resto2 = validação_digito2 % 11
if resto2 < 2:
    digito2 = 0
else:
    digito2 = 11 - resto2

cpf_completo = cpf_com_digito_1 + str(digito2)

# <<< correção: comparar CPF calculado com o digitado (sem pontuação)
cpf_validação = (cpf_completo == cpf_limpo)

# saída de dados:
if cpf_validação:
    print("CPF válido")
else:
    print("CPF inválido")
