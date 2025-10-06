ultimo = 10
ultimo2 = 1
fila = list(range(1,ultimo+1))
fila2 = list(range(1,ultimo2 +1))

while True:
        print(f"existem {len(fila)} clientes na fila")
        print(f"existem {len(fila2)} clientes na fila")

        
        print(f"fila 1 atual: {fila}")
        print(f"fila 2 atual: {fila2}")
        print(f"Digite F para adicionar um cliente na fila 1")
        print(f"Digite G para adicionar um cliente na fila 2")

        print(f"A para realizar o atendimento da fila 1")
        print(f"B para realizar o atendimento da fila 2")
        print(f"S para sair")

        operacao = input("Operacao [F],[G] [A],[B], [S]: ").upper()
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
            if operacao_valor == "B":
                if len(fila) > 0:
                    atendido = fila2.pop(0)
                    print(f"cliente {atendido} atendido")
                else:
                    print("Nenhum cliente e atender")
                    break
            elif operacao_valor == "F":
                ultimo += 1
                fila.append(ultimo)
            elif operacao_valor == "G":
                ultimo2 += 1
                fila.append(ultimo2)
            elif operacao_valor == ["S"]:
                break
            else:
                print("Opcao invalida! [F],[G] [A],[B], [S]:")
            x += 1






