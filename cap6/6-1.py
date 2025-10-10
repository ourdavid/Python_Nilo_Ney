notas = [0,0,0,0,0,0,0]
x = 0
soma = 0

while x < 7:
    notas[x] = int(input(f"Digite a nota {x+1}: "))
    soma += notas[x]
    x += 1

x = 0
while x < 7:
    print(f"nota {x+1}: {notas[x]}")
    x += 1

print(f"media {soma/x:.2f}")
