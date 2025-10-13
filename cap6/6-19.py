tabela = {
    "alface" : [1000,2.30],
    "batata" : [500,0.45],
    "tomate" : [2001, 1.20],
    "feijao" : [100,1,50],
    
}

while True:
    produto = input("Digite o produto: \n")
    qnt_vendida = int(input("Digite a qnt: \n"))

    vendas = [[produto,qnt_vendida]]
    tem = True
    total = 0

    for operacao in vendas:

        produto, quantidade = operacao
        if produto in tabela:
            print("vendas")
            preco = tabela[produto][1]
            custo = preco*quantidade
            print(f"{produto:12s}: {quantidade:3d} * {preco:6.2f} = {custo:6.2f}")
            tabela[produto][0] -= quantidade
            total += custo
        else:
            print("produto nao encontrado")
            tem = False


    if not tem:
        continue

    print(f" Custo total? {total:21.2f}\n")
    print(f"Estoqu\n ")

    for chaves,dados in tabela.items():
        print(f"descricao: ", chaves)
        print(f"quantidade: ", dados[0])
        print(f"preco: {dados[1]:6.2f}")

    sair = input("Sair [S]? ").lower()

    if sair == "s":
        break
