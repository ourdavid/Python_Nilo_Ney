#Escreva um programa que converta uma temperatura digitada
#em °C em °F. A fórmula para essa conversão é

#o calculo ta no livro.

celsius = int(input("Celsius para fahrente digite o valor: "))

# aqui vem o calculo do livro

fahrenheit = ( 9 * celsius ) / 5 + 32
print(f"Celsius: {celsius}º")
print(f"Calculo ( 9 * {celsius} ) / 5 + 32")
print(f"Fahrenheit: {fahrenheit}º")