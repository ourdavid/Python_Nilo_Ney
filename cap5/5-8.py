x = 4
y = 5

resultado = 0
contador = 0
texto = ""

while x > contador:
    resultado += y
    texto += f"{y}+"
    contador += 1

print(f"{texto[0:-1]} = {resultado}")
