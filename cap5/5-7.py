tabuada = int(input("Qual a Tabuada: "))
inicio = int(input("Digite o inicio da tabuada: "))
fim = int(input("Digite o fim da tabuada: "))

while inicio <= fim:
    print(f"{tabuada} x {inicio} = {tabuada * inicio}")
    inicio += 1
