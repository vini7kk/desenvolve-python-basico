#Dada uma lista de endereços web (URLs) que sempre começam com "www." e sempre terminam com ".com", use o conceito de fatiamento de listas
#  para criar uma lista dominios com o nome principal de todos os domínios, conforme exemplo a seguir. 

lista_url = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
dominios = []

for url in lista_url:
    # Pega a substring do índice 4 até -4, removendo "www." e ".com"
    dominio = url[4:-4]
    dominios.append(dominio)

print(dominios)