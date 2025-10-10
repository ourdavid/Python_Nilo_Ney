ultimo = 10
fila = list(range(1,ultimo+1))

while True:
    print(f"existem {len(fila)} clientes na fila")
    print(f"fila atual: {fila}")
    print(f"Digite F para adicionar um cliente na fila")
    print(f"ou A para realizar o atendimento. S para sair.")

    operacao = input("Operacao [F], [A], [S]: ").upper()

    if operacao == "A":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"cliente {atendido} atendido")
        else:
            print("Nenhum cliente e atender")
    elif operacao == "F":
        ultimo += 1
        fila.append(ultimo)
    elif operacao == ["S"]:
        break
    else:
        print("Opcao invalida! [F], [A], [S]:")




