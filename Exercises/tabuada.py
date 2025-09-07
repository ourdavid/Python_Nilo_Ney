#Tabuada
# O usuário digita um número e o programa mostra a tabuada dele de 1 a 10.

def tabuada_escolhida(numero):
    lista = range(1,11)
    print(lista)
    for numero_lista in lista:
        print(f'{numero_lista} x {numero} = {numero_lista * numero}')

while True:
    try:
        numero_digitado = int(input('Qual tabuada: '))
        break
    except (ValueError, TypeError):
        print('Digite um valor valido')

tabuada_escolhida(numero_digitado)

