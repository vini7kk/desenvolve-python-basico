#Escreva um programa que solicita o nome do usuário e o imprime em forma de escada, como indicado no exemplo a seguir.
    
    #Digite seu nome: Fulano
                     #F
                     #Fu
                     #Ful    
                     #Fula
                     #Fulan
                     #Fulano

nome = str(input("digite o seu nome: "))
tamanho = len(nome) + 1
for letra in range(1, tamanho):
    print(nome[:letra])