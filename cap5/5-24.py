n = int(input("Quantos números primos você quer imprimir? "))

contador_primos = 0   # quantos primos já achei
numero = 2            # primeiro número a testar

while contador_primos < n:
    # verificar se 'numero' é primo
    if numero == 2:
        primo = True
    elif numero % 2 == 0:
        primo = False
    else:
        primo = True
        divisor = 3
        while divisor < numero:
            if numero % divisor == 0:
                primo = False
                break
            divisor += 2
    
    # se for primo, imprime e soma no contador
    if primo:
        print(numero, end=" ")
        contador_primos += 1
    
    numero += 1  # passa para o próximo número
