# Escreva um programa que pergunte o salário do funcionário e
# calcule o valor do aumento. Para salários superiores a RS 1.250, calcule um
# aumento de 10%. Para os inferiores ou iguais, de 15%

salario = float(input("Digite seu salario: "))

if salario > 1.250:
    print(f"salario: R$ {salario:.2f}")
    print(f"aumento 10%, R$ {salario * (10 / 100)}")
    print(salario + (salario * (10/100)))

if salario <= 1.250:
    print(f"salario: R$ {salario:.2f}")
    print(f"aumento 10%, R${salario * (15 / 100)}")
    print(salario + (salario * (15/100)))