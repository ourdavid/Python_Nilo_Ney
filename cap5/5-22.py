tabuada = int(input("Tabuada: "))

while True:
    1
    print("operacao da tabuada")
    print("1) +")
    print("2) -")
    print("3) *")
    print("4) /")
    operacao = int(input("digite o numero da operacao"))

    numero = 1
    if operacao == 1:
        while numero <= 10:
            print(f"{tabuada} - {numero} = {tabuada + numero}")
            numero += 1 
    elif operacao == 2:
        while numero <= 10:
            print(f"{tabuada} - {numero} = {tabuada - numero}")
            numero += 1 
    elif operacao == 3:
        while numero <= 10:
            print(f"{tabuada} - {numero} = {tabuada * numero}")
            numero += 1 
    elif operacao == 4:
        while numero <= 10:
            print(f"{tabuada} - {numero} = {tabuada / numero}")
            numero += 1 

    saida = input("Sair : [s] ou [n]")
    if saida.lower() == "s":
        break