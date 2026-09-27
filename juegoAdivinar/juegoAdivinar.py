
'''
En Python per crear un número integer aleatori del 1 al 10:

import random

num = random.randint(1, 10)
print(num)

El programa "pensa" un número aleatori i fa un bucle demanant al usuari quin número ha pensat, 
si la diferencia entre el número que entra i el aleatori és major que 5 diu "Fred", en cas contrari "Calent", 
si l'encerta diu "Encertat" i acaba el programa.

'''


if __name__ == "__main__":
    import random

    secret = random.randint(1, 10)
    #print(secret)

   
    while True:
        numJugador = int(input("¿Qué número has pensado del 1 al 10? "))

        if numJugador == secret:
            print("Encertat")
            break
        else:
            diferencia = abs(numJugador - secret)
        if diferencia > 5:
            print("Fred")
        else:
            print("Calent")   
           
    print ("El número secreto era:", secret)



