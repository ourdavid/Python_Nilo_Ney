#Adicionar 3 nomes de amigos em uma lista vazia.
nomes = []


for x in range(1,4):

    if x == 1:
        a = f"digite o primeiro nome: "
    if x == 2:
        a = f"digite o segundo nome: "
    if x == 3:
        a = f"digite o terceiro nome: "

    nome = input(a)
    nomes.append(nome)

# while x < 3:

#     if x == 0:
#         a = f"digite o primeiro nome: "
#     if x + 1 == 1:
#         a = f"digite o segundo nome: "
#     if x + 1 == 2:
#         a = f"digite o terceiro nome: "

#     x += 1

print(nomes)