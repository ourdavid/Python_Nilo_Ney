#Escreva um programa que pergunte a velocidade do carro de um
#usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuá
#rio foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km
#acima de 80 km/h

velocidade = int(input("Digite a velocidade em Km/h: "))
multa = 5 * velocidade

if velocidade > 80:
    print(f"Multado : R$ {multa:.2f}")

if velocidade <= 80:
    print(f"Sem multa por km/h")
