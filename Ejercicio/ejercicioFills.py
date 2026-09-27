


import threading


def contar():

    contador = 0

    while contador < 100:

        contador+=1

        print('Hilo:',
        threading.current_thread().name,
        'con identificador:',
        threading.current_thread().ident,
        'Contador:', contador)

# = creo un hilo y le digo qué trabajo tendrá que hacer.
hilo1 = threading.Thread(target=contar)
hilo2 = threading.Thread(target=contar)
# = arranca el hilo y empieza a hacer ese trabajo.
hilo1.start()
hilo2.start()

        
