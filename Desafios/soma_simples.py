#Soma simples
#Peça dois números ao usuário e mostre a soma.
#Depois, modifique para somar 3 números.

def soma(x=0,y=0,z=0):
    return x+y+z

while True:

    try:
        valor1 = int(input("Digite um valor: "))
        valor2 = int(input(f"Digite outro valor {valor1} + : "))
        break

    except ValueError:
        print("digite um valor valido")

soma1 = soma(valor1,valor2)
print(soma1)

while True:
    try:
        valor1 = int(input("Digite um valor: "))
        valor2 = int(input(f"Digite outro valor {valor1} + : "))
        valor3 = int(input(f"Digite outro valor {valor1} + {valor2} + : "))
        break
    except ValueError:
        print("digite um valor valido")

print(soma(valor1,valor2,valor3))