#Reescreva o Programa 4.4 e calcule a conta da operadora Tchau
#usando else

plano = input("Digite o nome do plano: ")

if plano == "falapouco":
    minutos_do_plano = 100
    extra = 0.20
    preco = 50
else:
    minutos_do_plano = 500
    extra = 0.15
    preco = 99

if plano != "falapouco" and plano != "falamuito":
    print("plano inexistente")

if plano == "falapouco" or plano == "falamuito":
    minutos_consumidos = int(input("Quantos minutos consumiu: "))
    print(f"Preço do plano R$ {preco:.2f}")
    sumplemento = 0
    if minutos_consumidos >= minutos_do_plano:
        sumplemento = extra * (minutos_consumidos - minutos_do_plano)
        print(f"Sumamento do plano R$ {sumplemento:.2f}")
        print(f"total R$ {preco + sumplemento:.2f}")


