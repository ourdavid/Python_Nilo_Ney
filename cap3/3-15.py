# Entrada de dados
cigarros_por_dia = int(input("Quantidade de cigarros por dia: "))
anos_fumando = int(input("Quantos anos você já fumou? "))

minutos_perdidos_por_cigarro = 10

total_cigarros = cigarros_por_dia * anos_fumando * 365

total_minutos_perdidos = total_cigarros * minutos_perdidos_por_cigarro

total_dias_perdidos = total_minutos_perdidos / (60 * 24)

print(f"Você perdeu aproximadamente {total_dias_perdidos:.2f} dias de vida.")
