#reescrever o progama usando for em vez de while

# def soma(l):
#     total = 0 

#     x= 0 
#     while x <= 5:
#         total += l[x]
#         x += 1

#     return total

def soma(l):
    total = 0 

    for num in l:
        total += num

    return total
l = [1,7,2,9,15]

print(soma(l))
print(soma([7,9,12,3,100,20,4]))