#Contar quantas vezes um número aparece na lista [1,2,3,2,4,2].

lista = [1,2,3,4,5,2,3,4,5,1]

lista_contagem = []

tem = False


for num in lista:

    contador = 0
    repetido = False
    vezes = 0
    while len(lista_contagem) :

        if num != lista_contagem[contador]:
            lista_contagem.append(num)
        if repetido:
            vezes += 1
        
        contador += 1
    
    print(f"repetido {num} * {vezes}")


print(lista_contagem)
