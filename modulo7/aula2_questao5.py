# Implemente uma função chamada embaralhar_palavras() que recebe uma frase como entrada e retorna uma nova frase com 
# as letras internas de cada palavra embaralhadas. Mantenha sempre o primeiro e último caractere da palavra no lugar. 

import random

def embaralhar_palavras(frase):
    palavras = frase.split()  # divide a frase em lista de palavras
    resultado = []

    for palavra in palavras:
        # se a palavra tiver menos de 4 letras, não há "miolo" para embaralhar
        if len(palavra) <= 3:
            resultado.append(palavra)
        else:
            # separa o primeiro e o último caractere
            primeira = palavra[0]
            ultima = palavra[-1]
            meio = list(palavra[1:-1])  # transforma o meio em lista para embaralhar
            
            random.shuffle(meio)  # embaralha as letras do meio
            nova_palavra = primeira + ''.join(meio) + ultima
            resultado.append(nova_palavra)

    # junta tudo de volta em uma frase
    return ' '.join(resultado)
frase = input("Digite uma frase: ")
print("Frase embaralhada:", embaralhar_palavras(frase))