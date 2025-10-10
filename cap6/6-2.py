
numeros = [0,0,0,0,0]
x = 0

while x < 5:
    numeros[x] = int(input(f"Numero {x+1}: "))
    x += 1 

print(numeros)
while True:
    escolhindo = int(input(f"Que posicao voce quer imprimir (0 para sair): "))
    if escolhindo == 0:
        break
    print(f"Voce escolheu a posicao {numeros[(escolhindo-1)]}")
