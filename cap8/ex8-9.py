# Desafio: Rastreie o progama 8.6 e compare o seu resultado com o apresentado


def fatorial(n):
    print(f"calculando o fatorial de {n}")
    if n == 0 or n == 1:
        print(f"fatorial  de {n} = {1}")
        return 1
    else:
        fat = n* fatorial(n-1)
        print(f"fatorial de {n} = {fat}")
    return fat


fatorial(5)