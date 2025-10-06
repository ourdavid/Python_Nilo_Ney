# Faça um programa que percorra duas listas e gere uma terceira
# sem elementos repetidos.

l1 = [1,2,2,3,4,6]
l2 = [7,2,4,3,5,6,7]
l3 = []

x = 0
while x < len(l1):
    valor = l1[x]
    
    y = 0
    repetido = False
    while y < len(l3):
        if valor == l3[y]:
            repetido = True
        y += 1
    
    if repetido == False :
        l3.append(valor)
    x += 1

x = 0
while x < len(l2):
    valor = l2[x]
    
    y = 0
    repetido = False
    while y < len(l3):
        if valor == l3[y]:
            repetido = True
        y += 1
    
    if repetido == False :
        l3.append(valor)
    x += 1



print(l3)

