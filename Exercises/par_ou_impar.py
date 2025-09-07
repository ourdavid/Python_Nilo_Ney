#Par ou ímpar
#O usuário digita um número. O programa deve dizer se é par ou ímpar.

def verficador_par_impar(x):
    return "par" if x % 2 == 0 else "impar"

while True:
    try:
        numero = int(input("verificador de par ou impar: "))
        break
    except ValueError:
        print("digite um numero valido")

print(verficador_par_impar(numero))



