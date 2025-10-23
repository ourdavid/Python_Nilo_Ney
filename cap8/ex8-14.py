import random

n = random.randint(1,10)



for x in range(0,3):
    x = int(input("Digiten um numero entre 1 e 10: "))
    if x == n:
        print("Acertou!!")
        break
    else:
        print("Errou")