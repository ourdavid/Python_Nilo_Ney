deposito_inicial = float(input("Depósito inicial: "))
valor_mensal = float(input("Valor depositando mensalmente: "))
taxa_anual = float(input("Taxa de juros anual (%): "))

# converte a taxa anual para mensal
taxa_mensal = taxa_anual / 12

saldo = deposito_inicial
contador = 1

while contador <= 24:
    if contador > 1:  
        saldo += valor_mensal

    saldo += saldo * (taxa_mensal / 100)

    print(f"Mês [{contador}] - R$ {saldo:.2f}")
    contador += 1

total_depositado = deposito_inicial + valor_mensal * 23 
juros_total = saldo - total_depositado

print(f"\nSaldo final = R$ {saldo:.2f}")
print(f"Juros total = R$ {juros_total:.2f}")
