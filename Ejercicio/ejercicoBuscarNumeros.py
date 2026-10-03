
import threading
contador = 0

def es_primo(numero):
    if numero < 2:
        return False

    for i in range(2, numero -1):
        if numero % i == 0:
            return False

    return True






def buscaNP(*args):
    
    inicio = args[0]
    fin = args[1]

    for n in range(inicio, fin):
        if es_primo(n):
            global contador
            contador += 1
            print(n, "es primo")

           




f1 = threading.Thread ( target=buscaNP, args=( 2, 25000))
f2 = threading.Thread ( target=buscaNP, args=( 25001, 50000))

f1.start()
f2.start()
f1.join()
f2.join()

print(contador)






    
