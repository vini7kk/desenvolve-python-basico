#Implemente uma função em Python chamada validador_senha() que verifica se uma senha fornecida atende todos os 
#seguintes critérios:
    #Pelo menos 8 caracteres de comprimento.
    #Contém pelo menos uma letra maiúscula e uma letra minúscula.
    #Contém pelo menos um número.
    #Contém pelo menos um caractere especial (por exemplo, @, #, $).


# Implementação da função validador_senha()

def validador_senha(senha):
    especiais = "!@#$%^&*()-_=+[{]};:',<.>/?|\\"
    numeros = "0123456789"
    
    if len(senha) < 8:
        return "Senha inválida: deve conter no mínimo 8 caracteres."
    
    if not any(c.islower() for c in senha):
        return "Senha inválida: deve conter pelo menos uma letra minúscula."
    
    if not any(c.isupper() for c in senha):
        return "Senha inválida: deve conter pelo menos uma letra maiúscula."
    
    if not any(c in numeros for c in senha):
        return "Senha inválida: deve conter pelo menos um número."
    
    if not any(c in especiais for c in senha):
        return "Senha inválida: deve conter pelo menos um caractere especial."
    
    return "Senha aprovada!"


# Instruções para o usuário
print("Para criar sua senha, é necessário:")
print("- Pelo menos 8 caracteres de comprimento.")
print("- Pelo menos uma letra maiúscula e uma letra minúscula.")
print("- Pelo menos um número.")
print("- Pelo menos um caractere especial (por exemplo, @, #, $).")

# Solicitação e verificação em loop
while True:
    senha = input("\nInsira a senha: ")
    resultado = validador_senha(senha)
    print(resultado)
    
    if resultado == "Senha aprovada!":
        break