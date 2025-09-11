#Escreva um programa que pergunte a quantidade de km percor
#ridos por um carro alugado pelo usuário, assim como a quantidade de dias
#pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro
#custa R$ 60 por dia e R$ 0,15 por km rodado.

km_pecorridos = float(input("Km pecridos: "))
qtd_de_dias = float(input("Quantidade de dias: "))

aluguel_carro_dia = 60
km_preco = 0.15
total = (qtd_de_dias * aluguel_carro_dia) + (km_pecorridos * km_preco)

print(f"Total: {total}")
