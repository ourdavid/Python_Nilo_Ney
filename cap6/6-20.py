frase = "O rato"

dicinario = {}

contador = 0
for letra in frase:
    if letra != " ":

        dicinario[letra] = contador 
        contador += 1
        


print(dicinario.items())

