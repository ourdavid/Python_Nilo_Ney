numero = [10,13,230]

while True:
    n = int(input("Digite o numero que deseja achar: "))
    contador = 0
    while contador < len(numero):
        if numero[contador] == n:
            print(f"Achou o numero {numero[contador]} na posicao {contador}")
            break
        contador += 1
    
    if contador == len(numero):
        print(f"nao achou")
        break
    