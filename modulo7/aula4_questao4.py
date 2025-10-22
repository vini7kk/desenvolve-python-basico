import random

# Função que imprime o enforcado conforme o número de erros
def imprime_enforcado(erros, estagios):
    print(estagios[erros])

# Lê o arquivo com as palavras da forca
with open("gabarito_forca.txt", "r", encoding="utf-8") as arquivo:
    palavras = arquivo.read().splitlines()

# Lê o arquivo com os estágios do enforcado
with open("gabarito_enforcado.txt", "r", encoding="utf-8") as arquivo:
    estagios = arquivo.read().split("\n\n")  # separa cada estágio

# Escolhe uma palavra aleatória
palavra_secreta = random.choice(palavras).lower()

# Cria a lista de underscores
progresso = ["_" for _ in palavra_secreta]

# Variáveis de controle
erros = 0
max_erros = 6
letras_erradas = []

print("=== JOGO DA FORCA ===")
print("Adivinhe a palavra!")
print(" ".join(progresso))

# Loop principal do jogo
while erros < max_erros and "_" in progresso:
    tentativa = input("\nDigite uma letra: ").lower()

    # Validação da entrada
    if len(tentativa) != 1 or not tentativa.isalpha():
        print("Digite apenas uma letra válida.")
        continue

    # Caso a letra já tenha sido usada
    if tentativa in progresso or tentativa in letras_erradas:
        print("Você já tentou essa letra!")
        continue

    # Se a letra estiver na palavra
    if tentativa in palavra_secreta:
        for i, letra in enumerate(palavra_secreta):
            if letra == tentativa:
                progresso[i] = tentativa
        print("\nBoa! Letra correta!")
    else:
        erros += 1
        letras_erradas.append(tentativa)
        print("\nLetra errada!")
        imprime_enforcado(erros, estagios)

    # Mostra o progresso e letras erradas
    print("\n Palavra:", " ".join(progresso))
    print("Letras erradas:", ", ".join(letras_erradas))

# Verifica resultado final
if "_" not in progresso:
    print("\n Parabéns, você venceu! A palavra era:", palavra_secreta)
else:
    print("\n Fim de jogo! A palavra era:", palavra_secreta)
