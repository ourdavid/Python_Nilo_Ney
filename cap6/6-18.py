# buble sort
# deixar na ordem descrecente ?
lista = [1,2,3,4,5,6]

fim = len(lista)

contador = 0
while fim > 1:
    trocou = False
    x = 0

    while x < (fim -1):
        if lista[x] < lista[x+1]:
            trocou = True
            temp = lista[x]
            lista[x] = lista[x+1]
            lista[x+1] = temp
        x += 1
    if not trocou:
        break
    fim -= 1

for e in lista:
    print(e)