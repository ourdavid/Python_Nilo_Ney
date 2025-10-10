# A lista de temperaturas de Mons, na Bélgica, foi armazenada na
# lista T = [ -10, -8, 0, 1, 2, 5, -2, -4]. Faça um programa que imprima a menor
# e a maior temperatura, assim como a temperatura média.

t = [ -10, -8, 0, 1, 2, 5, -2, -4]

maior = t[0]
menor = t[0]
media = 0
for temperatura in t:
    media += temperatura
    if temperatura > maior:
        maior = temperatura
    if temperatura < menor:
        menor = temperatura

media = media / len(t)
print(media)
print(maior)
print(menor)