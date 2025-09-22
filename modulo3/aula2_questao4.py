#Você é mestre de uma mesa de RPG e vai criar um sistema para validar uma ficha de personagem. Cada personagem tem uma classe específica 
#com requisitos de atributos. Escreva um script que solicita a classe de personagem escolhida (guerreiro, mago ou arqueiro), os pontos de
#força e os pontos de magia atribuídos ao personagem. O programa deve imprimir True se os pontos de atributo são consistentes com a 
#classe escolhida, seguindo as seguintes regras:

#Guerreiro: Força deve ser igual ou superior a 15, Magia deve ser 10 ou menos.

#Mago: Força deve ser 10 ou menos, Magia deve ser igual ou superior a 15.

#Arqueiro: Força e Magia devem ser ambos superiores a 5, mas nenhum deles pode ser superior a 15.

#O programa deve imprimir False se os pontos de atributo não são consistentes com a classe escolhida. 



########## entrada de dados

classe = str(input("Escolha a classe (guerreiro, mago ou arqueiro): "))
força = int(input("Digite os pontos de força (de 1 a 20):" ))
magia = int(input("Digite os pontos de magia (de 1 a 20):" ))


#processamento

if classe == 'guerreiro' and força >= 15 and magia <= 10:  
    personagem = True

elif classe == 'mago' and força <= 10 and magia >= 15:
    personagem = True

elif classe == 'arqueiro' and força >= 5 and magia >= 5 and força <= 15 and magia <= 15:
    personagem = True
else: 
    personagem = False

#saida de dados

print(personagem)