#Criar uma lista com 5 números e imprimir o maior e o menor.

lista = [1,2,3,4,5]

maior = lista[0]
menor = lista[0]

for numero in lista:
    if numero > maior:
        maior = numero
    
    if numero < menor:
        menor = numero

print(f"Maior : {maior}")
print(f"Menor : {menor}")