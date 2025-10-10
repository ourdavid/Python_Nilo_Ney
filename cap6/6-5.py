ultimo = 10
fila = list(range(1,ultimo+1))

while True:
    print(f"existem {len(fila)} clientes na fila")
    print(f"fila atual: {fila}")
    print(f"Digite F para adicionar um cliente na fila")
    print(f"ou A para realizar o atendimento. S para sair.")

    operacao = input("Operacao [F], [A], [S]: ").upper()
    x = 0
    while x < len(operacao):
        operacao_valor = operacao[x]
        if operacao_valor == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"cliente {atendido} atendido")
            else:
                print("Nenhum cliente e atender")
                break
        elif operacao_valor == "F":
            ultimo += 1
            fila.append(ultimo)
        elif operacao_valor == ["S"]:
            break
        else:
            print("Opcao invalida! [F], [A], [S]:")

        x += 1






