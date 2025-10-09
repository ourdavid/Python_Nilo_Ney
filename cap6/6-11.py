# modificar o progama 6.6 do livro que esta usando while so que pro for

l = []
while True:
    n = int(input("Digite um numero (0 sair): "))
    if n == 0:
        break

    l.append(n)

for item in l:
    print(item)
