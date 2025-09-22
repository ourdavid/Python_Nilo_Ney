while True:
    n = int(input("Verificador de numero primo: "))
    if n <= 1:
        print("nao e numero primo")
    elif n == 2:
        print("Unico numero primo par [ 2 ]")
    elif n % 2 == 0 :
        print("nao e numero primo")
    else:
        primo = True
        divisor = 3

        while divisor < n:
            if n % divisor == 0:
                primo = not primo
                break
            divisor += 2
        
        print(f"{n} e primo") if primo else print(f"{n} nao e primo")