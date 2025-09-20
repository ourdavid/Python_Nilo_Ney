# Escreva um programa para controlar uma pequena máquina
# registradora. Você deve solicitar ao usuário que digite o código do produto e a
# quantidade comprada. Utilize a tabela de códigos a seguir para obter o preço
# de cada produto:

total = 0
while True:

    codigo = int(input("Codigo: "))
    if codigo ==0:
        break
    qtd_comprada = int(input("Quantidade: "))

    
    if codigo == 1:
        preco = 0.50
        total += qtd_comprada * preco
    elif codigo == 2:
        preco = 1.00
        total += qtd_comprada * preco
    elif codigo == 3:
        preco = 3.00
        total += qtd_comprada * preco
    elif codigo == 5:
        preco = 1.00
        total += qtd_comprada * preco
    elif codigo == 9:
        preco = 9.00
        total += qtd_comprada * preco
    else:
        print("codigo invalido")
    
print(f"\n Valor Total: {total}")

