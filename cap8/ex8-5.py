def soma(lista):
    total = 0

    for numeros in lista:
        total += numeros

    return total

def media(l):

    return soma(l) / len(l)

def fatorial(n):

    fat = 1

    while n > 1:
        fat *= n
        n -= 1

    return fat


l = [10,20,25,30]


print(soma(l))
print(media(l))

print(fatorial(3))