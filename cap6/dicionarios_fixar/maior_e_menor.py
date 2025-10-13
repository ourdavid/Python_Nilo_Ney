l = [1,2,3,4,5]

maior = l[0]
menor = l[0]

for numero in l:
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero


print(f"Maior = {maior} menor = {menor}")