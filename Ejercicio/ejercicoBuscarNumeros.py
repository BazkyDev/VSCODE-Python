def es_primo(numero):
    if numero < 2:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


numero = 28
print(f"¿El número {numero} es primo? {es_primo(numero)}")



def llistaPrimer(*args):
    numeroInicial = args[0]
    numeroFinal = args[1]



    #(2,25000)
    #(25000, 50000)




    
