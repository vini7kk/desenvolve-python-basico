#Escreva um programa em Python que solicita ao usuário para inserir a avaliação de um filme em uma escala de 1 a 5. O programa deve 
# imprimir uma mensagem correspondente à classificação do filme:

#Se a avaliação for 5, imprima "Excelente!"
#Se a avaliação for 4, imprima "Muito Bom!"

#e a avaliação for 3, imprima "Bom!"
#Se a avaliação for 2, imprima "Regular."
#Se a avaliação for 1, imprima "Ruim."


#entrada
nota = int(input("avalie o filme numa escala de 1-5: "))
#processamento


if nota == 5:
    txt = "Excelente!"

elif nota == 4:
    txt = "Muito Bom!"

elif nota == 3:
    txt = "Bom!"

elif nota == 2:
    txt = "Regular."

elif nota == 1:
    txt = "Ruim."

#saida


print(f"Você avaliou o filme como: {txt}")