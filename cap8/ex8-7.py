#crie uma funcao recursiva que calcule o mairo divisor comum entre dois numeros a e b em que a > b:

def mdc(a,b):

    if b == 0:
        return a
    else:
        return mdc(b, a% b)

print(mdc(8,6))