#Escreva um programa que calcule o tempo de uma viagem de
#carro. Pergunte a distância a percorrer e a velocidade média esperada para a
#viagem.

distacia = int(input("Distancia em km: "))
valocidade_media_esperada = int(input("Velocidade media esperada: "))

tempo = distacia/valocidade_media_esperada

horas = int(tempo)
minutos = int((tempo - horas) * 60)

print(f"Tempo estimado de viagem: {horas}h {minutos}min")

