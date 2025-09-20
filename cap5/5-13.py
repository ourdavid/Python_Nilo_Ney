# Escreva um programa que pergunte o valor inicial de uma dívida
# e o juro mensal. Pergunte também o valor mensal que será pago. Imprima o
# número de meses para que a dívida seja paga, o total pago e o total de juros
# pago.

valor_inicial_divida = float(input("Valor inicial da divida: ")) 
juro_mensal = float(input("Juros mensal: "))
valor_mensal_pagar = float(input("Valor mensal que sera pago: "))

total_pago = 0
total_juros = 0

meses = 0
contador = 0

if valor_mensal_pagar <= valor_inicial_divida * juro_mensal:
    print("divida nunca sera paga.")
else:
    while valor_inicial_divida > 0:
        juro_mes = valor_inicial_divida * juro_mensal
        valor_inicial_divida += juro_mes
        total_juros += juro_mes

        valor_inicial_divida -= valor_mensal_pagar
        total_pago += valor_mensal_pagar
        meses += 1

    print(f"Meses para divida ser quitada: {meses}")
    print(f"Total pago : {total_pago:.2f}")
    print(f"Total de juros pago: {(total_juros):.0f} ")


    

