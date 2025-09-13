#Escreva um programa que leia três números e que imprima o maior e o menor.

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
num3 = int(input("Digite mais um numero: "))

if num1 > num2 and num1 > num3:
    print(f" Maior numero {num1}")
if num2 > num1 and num2 > num3:
    print(f" Maior numero {num2}")
if num3 > num1 and num3 > num2:
    print(f" Maior numero {num3}")

if num1 < num2 and num1 < num3:
    print(f" Menor numero {num1}")
if num2 < num1 and num2 < num3:
    print(f" Menor numero {num2}")
if num3 < num1 and num3 < num2:
    print(f" Menor numero {num3}")
