#Leia 5 nomes e armazene em uma lista. Depois, mostre os nomes em ordem alfabética

nomes = []

for e in range(0,5):

    nome = input("digite: ").lower()
    nomes.append(nome.lower())

nomes.sort()

for nome in nomes:
    print(nome.capitalize())