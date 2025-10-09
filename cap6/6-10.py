# Prograna 6.9: Pesquisa sequencial
L = [15, 7, 27, 39]
p = int(input("Numero a procurar [p]: "))
v = int(input("Numero a procurar [v]: "))

achou = False
x = 0
while x < len(L):
    if L[x] == p:
        print(f"p = {p} Encotrando na  posicao [{x}]")
        achou = True
    x += 1

if achou == False:
    print(f"p = {p} nao encontrado")


achou = False
x = 0
while x < len(L):
    if L[x] == v:
        print(f"v = {v} Encotrando na  posicao [{x}]")
        achou = True
    x += 1

if achou == False:
    print(f"v = {v} nao encontrado")