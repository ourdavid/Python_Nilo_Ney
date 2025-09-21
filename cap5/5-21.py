while True:
    valor = int(input(f"Digite o valor a pagar (0 para sair): "))
    if valor == 0:
        break

    apagar = valor
    cedulas = 0
    atual = 100

    while True:
        if atual <= apagar: # se atual for menor que apagar
            apagar -= atual # apagar - atual
            cedulas += 1 # adiciona uma cedula na variavel
        else: # caso atual nao for menor que apagar
            if cedulas > 0 :
                print(f"{cedulas}, cedulas(s) de R${atual}")

            if apagar == 0:
                break

            if atual == 100:
                atual = 50
            elif atual == 50:
                atual = 20
            elif atual == 20:
                atual = 10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 1
            cedulas = 0