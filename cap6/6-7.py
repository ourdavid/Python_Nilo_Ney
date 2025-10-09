expressao = "())"
pilha = []

x = 0
erro = False


while x < len(expressao):

    simbolo = expressao[x]

    if simbolo == "(":
        pilha.append("(")
    elif simbolo == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            erro = True
            break
    x += 1

if erro == False and len(pilha) == 0:
    print(f"{expressao} = Ok")
else:
    print(f"{expressao} = erro")