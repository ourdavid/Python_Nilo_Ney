import os

def soma (x,y):
    os.system("clear")
    return f"{x} + {y} = {x+y}"

def multiplica (x,y):
    os.system("clear")
    return f"{x} * {y} = {x*y}"

def subtracao (x,y):
    os.system("clear")
    return f"{x} - {y} = {x-y}"

def divisao (x,y):
    if y == 0:
        return f"Divisao por zero e impossivel."
    else:
        os.system("clear")
        return f"{x} / {y} = {x/y}"
   

def msg():
    while True: 
        try:
            print("1) +")
            print("2) -")
            print("3) *")
            print("4) /")
            operador = int(input("Digite o operador : "))
    
            if operador == 1:
                numero2 = float(input("Digite o segundo numero: "))
                print(soma (numero1,numero2))
                break
            elif operador == 2:
                numero2 = float(input("Digite o segundo numero: "))
                print(subtracao (numero1,numero2))
                break
            elif operador == 3:
                numero2 = float(input("Digite o segundo numero: "))
                print(multiplica (numero1,numero2))
                break
            elif operador == 4:
                numero2 = float(input("Digite o segundo numero: "))
                print(divisao (numero1,numero2))
                break
            else:
                print("digite uma opcao valida!!")
                continue
        except ValueError:
            print("Digite um valor valido.")
        

while True:
    os.system("clear")
    try:
        numero1 = float(input("Digite primeiro numero: "))
    except ValueError:
        print("digite um numero valido!!")

    msg()
    
    sair = input("sair [S]im ou [N]ao? ").lower()
    if sair == "s":
        break

        

