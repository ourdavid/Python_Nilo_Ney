#Faça um programa que calcule o aumento de um salário. Ele
#deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor
#do aumento e do novo salário

salario = float(input("Digite o salario: "))
porcentagem_aumento = int(input("Digite a porcentagem de aumento ex [15]: ")) / 100

print(salario + (salario * porcentagem_aumento))
