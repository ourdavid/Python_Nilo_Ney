#Escreva uma funcao que retorne o maior de dois numeros:

def maximo(x,y):

    if x > y:
        return f"{x} maior que {y}"
    elif x < y: 
        return f"{y} maior que {x}"
    else:
        return f"{x} == {y}"
    



print(maximo(2,1))
print(maximo(3,4))
print(maximo(4,4))