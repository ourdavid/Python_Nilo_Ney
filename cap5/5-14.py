# Escreva um programa que leia números inteiros do teclado. O pro
# grama deve ler os números até que o usuário digite 0 (zero). No final da execu
# ção, exiba a quantidade de números digitados, assim como a soma e a média
# aritmética.

numeros_digitados = 0
soma = 0

while True:

    numero = int(input("Digite o numero: "))
    if numero == 0:
        break

    soma += numero
    numeros_digitados +=1 

if numeros_digitados > 0:
        media = soma / numeros_digitados
        print(f"Quantidade de numeros digitados: {numeros_digitados}")
        print(f"Soma = {soma}")
        print(f"Media aritmetica = {media}")
else:
     print("nenhum numero digitado")

