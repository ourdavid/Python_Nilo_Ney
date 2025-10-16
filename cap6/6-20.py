dicionario_frase = {}

for letra in "O rato":
    if letra in dicionario_frase:
        dicionario_frase[letra] = dicionario_frase.get(letra, 0) + 1
    else:
        dicionario_frase[letra] = 1


print(dicionario_frase)
