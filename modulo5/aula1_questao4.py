#Escreva um programa em Python que utiliza a biblioteca datetime para exibir a data e hora atuais com a formatação apresentada a seguir:
# Data: 15/03/2023 
# Hora: 14:05

from datetime import datetime

agora = datetime.now()
print(agora.strftime("%d/%m/%Y"))        # dia/mes/ano
print(agora.strftime("%H:%M:%S"))        # hora/minutos/segundos

