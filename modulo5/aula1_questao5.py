# Importa a função emojize da biblioteca emoji
from emoji import emojize

# Dicionário de emojis sugeridos
emojis_disponiveis = {
    "❤️": ":red_heart:",
    "👍": ":thumbs_up:",
    "🤔": ":thinking_face:",
    "🥳": ":partying_face:"
}

# Mostra a lista de emojis para o usuário
print("Emojis disponíveis:\n")
for emoji_char, emoji_text in emojis_disponiveis.items():
    print(f"{emoji_char} - {emoji_text}")

# Solicita a frase do usuário
frase = input("\nDigite uma frase e ela será emojizada:\n")

# Converte o texto com códigos de emojis para emojis reais
frase_emojizada = emojize(frase, language="alias")

# Mostra a frase emojizada
print("\nFrase emojizada:\n")
print(frase_emojizada)
