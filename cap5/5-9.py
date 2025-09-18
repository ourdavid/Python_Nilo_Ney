dividendo = 20
divisor = 4

if divisor == 0:
    print("Divisao por zero nao e permitida")
else:
    quociente = 0
    resto = dividendo

while resto >= divisor:
    resto -= divisor
    quociente += 1

print(quociente)
print(resto)