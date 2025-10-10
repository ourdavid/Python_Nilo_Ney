# modificar o progamaw de forma a imprimir o menor numero da lista

# l = [1,2,3,4,5,6,7]

# maximo = l[0]

# for e in l:
#     if e > maximo:
#         maximo = e


l = [1,2,3,4,5,6,7]

menor = l[0]

for e in l:
    if e < menor:
         menor = e

print(menor)