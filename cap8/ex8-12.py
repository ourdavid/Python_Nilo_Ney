# Escreva uma funcao para valdiar uma string e uma lista.
# Essa funcao deve comparar a string passada com os elementso da lista,tambem passada como paramentro
# retorne verdadeiro se a tring for encontrada dentro da lista e falso caso contrario.

def validacao_string(string,lista):

    return string in lista
    

print(validacao_string("david",["caju","feijao"]))