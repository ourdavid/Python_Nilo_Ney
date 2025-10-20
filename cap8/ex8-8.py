# usando a funcao mdc definida no exercicio anteriro defina uma funcao para calcular o menor multiplo comum

def mdc(a,b):

    if b == 0:
        return a
    else:
        return mdc(b, a% b)


def mmc(a,b):
    mdc_resultado = mdc(a,b)
    
    return abs(a * b) / mdc_resultado


print(mmc(8,6))