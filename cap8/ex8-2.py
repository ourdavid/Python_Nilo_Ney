#escreva uma funcao que receba dois numeros e retorne True se o primeiro numero for multiplo do segundo

def multiplo(x,y):

    if x % y == 0:
        return True
    else:
        return False
    


print(multiplo(8,4))
print(multiplo(7,3))
print(multiplo(5,5))