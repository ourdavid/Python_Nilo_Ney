#Escreva um programa que pergunte a distância que um passa
#geiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50
#por km para viagens de até de 200 km, e RS 0,45 para viagens mais longas

distancia_desejada = int(input("Distancia de desejada? "))

passagem = 0.5
total = 0

if distancia_desejada < 200:
    total = distancia_desejada * passagem
    print(f"Total: R${total:.2f}")
else:
    total = distancia_desejada * 0.45
    print(f"Total: R${total:.2f}")

