numero = [10,13,230]

while True:
    p = int(input("Digite o numero  p que deseja achar: "))
    v = int(input("Digite o numero v que deseja achar: "))

    achado_p = -1
    achado_v = -1

    contador = 0
    while contador < len(numero):
        if numero[contador] == p and achado_p == -1:
            achado_p = contador
        if numero[contador] == v and achado_v == -1:
            achado_v = contador
        
        contador += 1
    
    contador = 0
    if achado_p == -1 and achado_v == -1:
        print("Nenhum dos dois valores foi achado")
    elif achado_p != -1 and achado_v == -1:
        print(f"Achado apenas o numero p {p} na posição {achado_p}")
    elif achado_v != -1 and achado_p == -1:
        print(f"Achado apenas o numero v {v} na posição {achado_v}")
    else:
        if achado_p < achado_v:
            print(f"o numero p {p}, foi achado primeiro na posicao {achado_p}")
        if achado_v < achado_p:
            print(f"o numero v {v}, foi achado primeiro na posicao {achado_v}")
        else:
            print(f"os dois estao na mesma posicao")

    
    if contador == len(numero):
        print(f"nao achou")
        break
    