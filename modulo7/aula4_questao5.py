# Criação do arquivo CSV com informações sobre livros

# Abre (ou cria) o arquivo para escrita
with open("meus_livros.csv", "w", encoding="utf-8") as arquivo:
    # Escreve o cabeçalho
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")

    # Escreve os dados dos livros
    arquivo.write("O Caçador de Pipas,Khaled Hosseini,2003,368\n")
    arquivo.write("Torto Arado,Itamar Vieira Junior,2019,264\n")
    arquivo.write("1984,George Orwell,1949,328\n")
    arquivo.write("Dom Casmurro,Machado de Assis,1899,256\n")
    arquivo.write("O Pequeno Príncipe,Antoine de Saint-Exupéry,1943,96\n")
    arquivo.write("A Menina que Roubava Livros,Markus Zusak,2005,480\n")
    arquivo.write("Orgulho e Preconceito,Jane Austen,1813,416\n")
    arquivo.write("O Hobbit,J.R.R. Tolkien,1937,310\n")
    arquivo.write("A Revolução dos Bichos,George Orwell,1945,112\n")
    arquivo.write("Cem Anos de Solidão,Gabriel García Márquez,1967,417\n")

# Ao final do bloco 'with', o arquivo é automaticamente fechado e salvo

print("Arquivo 'meus_livros.csv' criado com sucesso!")
