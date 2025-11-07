import csv

# Abrir o arquivo CSV no modo de leitura com codificação 'latin-1'
with open("spotify-2023.csv", "r", encoding="latin-1") as arquivo:
    leitor = csv.reader(arquivo)
    
    # Ler o cabeçalho (primeira linha)
    cabecalho = next(leitor)
    print("Cabeçalho das colunas:", cabecalho)
    
    # Exibir as 5 primeiras linhas para entender a estrutura
    print("\nPrimeiras 5 linhas do arquivo:")
    for i in range(5):
        print(next(leitor))

# Agora, reabrimos o arquivo para processar os dados
with open("spotify-2023.csv", "r", encoding="latin-1") as arquivo:
    leitor = csv.DictReader(arquivo)
    
    # Dicionário para armazenar a música mais tocada por ano
    mais_tocadas_por_ano = {}

    for linha in leitor:
        try:
            # Verificar se a linha é válida (sem aspas extras)
            texto = ",".join(linha.values())
            if '"' in texto:
                continue  # Ignora linhas com aspas, conforme o enunciado

            # Extrair os campos necessários
            nome = linha["track_name"]
            artista = linha["artist(s)_name"]
            ano = int(linha["released_year"])
            streams = int(linha["streams"])

            # Considerar apenas músicas entre 2012 e 2022
            if 2012 <= ano <= 2022:
                # Atualiza a música mais tocada daquele ano, se aplicável
                if (ano not in mais_tocadas_por_ano) or (streams > mais_tocadas_por_ano[ano][3]):
                    mais_tocadas_por_ano[ano] = [nome, artista, ano, streams]
        
        except Exception:
            # Ignora qualquer erro de conversão ou formato
            continue

# Converter o dicionário em uma lista ordenada por ano
resultado = [mais_tocadas_por_ano[ano] for ano in sorted(mais_tocadas_por_ano)]

# Exibir a lista final
print("\nMúsicas mais tocadas de 2012 a 2022:")
for item in resultado:
    print(item)
