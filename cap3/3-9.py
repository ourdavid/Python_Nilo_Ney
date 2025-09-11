#escreva um programa que leia a quantidade de dias, horas, minu
#tos e segundos do usuário. Calcule o total em segundos.

dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

dias_segundos = dias * 24 * 60 * 60
horas_segundos = horas * 60 * 60
minutos_segundos = minutos * 60
segundos = segundos

print(f"segundos: {dias_segundos + horas_segundos + minutos_segundos + segundos}")