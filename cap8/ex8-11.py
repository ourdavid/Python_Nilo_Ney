# Escreva uma funcao para valdiar uma variavel string.
# Essa funcao recebo como paramentro a string, o numero minimo e maximo de caracteres.
# retorne veradeiro se o tamanho da string estiver entre os valores de maximo e minimo e falso caso contrario

def validacao_string(string,minimo,maximo):

    if len(string) >= minimo and len(string) <= maximo:
        return True
    else:
        return False
    

print(validacao_string("david",1,5))